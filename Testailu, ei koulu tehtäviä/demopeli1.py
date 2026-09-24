
import random
import math
import mysql.connector


def etaisyys_km(lat1, lon1, lat2, lon2):
    """Laskee kahden koordinaatin valisen etaisyyden kilometreina."""
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(a))

# ---------------------------------------------------------------
# YHTEYS TIETOKANTAAN - vaihda omat tietosi
# ---------------------------------------------------------------

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="atte",
    password="140507"
)
kursori = yhteys.cursor(dictionary=True)

# ---------------------------------------------------------------
# ALUSTUS
# ---------------------------------------------------------------

KOTIKENTTA = "EFHK"
TAVOITE_RAHA = 300

raha = 0
polttoaine = 5000
sijainti = KOTIKENTTA
pelaaja_nimi = input("Anna nimimerkkisi: ")

# Haetaan kotikentän koordinaatit, jotta etaisyyksia voi laskea
kursori.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (sijainti,)
)
rivi = kursori.fetchone()
oma_lat = rivi["latitude_deg"]
oma_lon = rivi["longitude_deg"]
koti_lat = oma_lat
koti_lon = oma_lon

print("")
print("Tervetuloa lentopeliin,", pelaaja_nimi)
print("Kerää", TAVOITE_RAHA, "rahaa ja palaa kotikentälle", KOTIKENTTA)

# ---------------------------------------------------------------
# PELISILMUKKA
# ---------------------------------------------------------------

pelissa = True

while pelissa:

    print("")
    print("----------------------------------------")
    print("Olet kentällä:", sijainti)
    print("Rahaa:", raha, "/", TAVOITE_RAHA)
    print("Polttoainetta:", polttoaine, "km")
    print("----------------------------------------")

    # Voitto: kotona ja tarpeeksi rahaa
    if sijainti == KOTIKENTTA and raha >= TAVOITE_RAHA:
        print("Voitit pelin! Palasit kotiin", raha, "rahan kanssa.")
        break

    # Haetaan 5 satunnaista kenttää tietokannasta, koordinaatit mukaan
    kursori.execute(
        "SELECT ident, name, municipality, latitude_deg, longitude_deg FROM airport "
        "WHERE type = 'large_airport' AND continent = 'EU' AND ident != %s "
        "ORDER BY RAND() LIMIT 5",
        (sijainti,)
    )
    kentat = kursori.fetchall()

    # Lasketaan etaisyys jokaiseen kenttaan etukateen ja tallennetaan se listaan
    matkat = []
    for kentta in kentat:
        matka = etaisyys_km(oma_lat, oma_lon, kentta["latitude_deg"], kentta["longitude_deg"])
        matkat.append(matka)

    print("Minne haluat lentää?")
    print("0. Lopeta peli")
    if sijainti != KOTIKENTTA:
        koti_matka = etaisyys_km(oma_lat, oma_lon, koti_lat, koti_lon)
        print("9. Lennä kotiin (", KOTIKENTTA, ") -", round(koti_matka), "km")

    numero = 1
    for kentta in kentat:
        print(numero, ".", kentta["name"], "(" + kentta["ident"] + ")", "-", kentta["municipality"],
              "-", round(matkat[numero - 1]), "km")
        numero = numero + 1

    valinta = input("Valintasi: ")

    if valinta == "0":
        print("Peli lopetettu.")
        break

    elif valinta == "9" and sijainti != KOTIKENTTA:
        matka = etaisyys_km(oma_lat, oma_lon, koti_lat, koti_lon)
        if matka > polttoaine:
            print("Polttoaine ei riitä kotiin! Tarvitset", round(matka), "km.")
        else:
            polttoaine = round(polttoaine - matka)
            sijainti = KOTIKENTTA
            oma_lat = koti_lat
            oma_lon = koti_lon
            print("Lensit", round(matka), "km kotikentälle.")

    elif valinta.isdigit() and 1 <= int(valinta) <= len(kentat):
        indeksi = int(valinta) - 1
        kohde = kentat[indeksi]
        matka = matkat[indeksi]

        if matka > polttoaine:
            print("Polttoaine ei riitä! Tarvitset", round(matka), "km, sinulla on", polttoaine, "km.")
        else:
            polttoaine = round(polttoaine - matka)
            sijainti = kohde["ident"]
            oma_lat = kohde["latitude_deg"]
            oma_lon = kohde["longitude_deg"]
            print("Lensit", round(matka), "km kentälle", kohde["name"])

            loyto = random.randint(50, 150)
            raha = raha + loyto
            print("Löysit", loyto, "rahaa!")

    else:
        print("Virheellinen valinta, yritä uudelleen.")

    if polttoaine <= 0:
        print("Polttoaine loppui. Peli päättyi.")
        break

# ---------------------------------------------------------------
# LOPETUS
# ---------------------------------------------------------------

kursori.close()
yhteys.close()