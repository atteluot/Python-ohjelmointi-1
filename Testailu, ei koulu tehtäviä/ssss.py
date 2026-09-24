"""
Lentopeli - yksinkertainen runko
--------------------------------
Lennä kentältä toiselle, kerää rahaa ja palaa kotikentalle
ennen kuin polttoaine loppuu.

Vaatii: pip install mysql-connector-python
"""

import math
import random
import mysql.connector

# ---------------------------------------------------------------
# ASETUKSET - muuta nama omaan ymparistoosi sopiviksi
# ---------------------------------------------------------------

YHTEYS_TIEDOT = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "flight_game",
    "user": "atte",
    "password": "140507",
    "autocommit": True,
    "collation": "utf8mb4_general_ci",
}

KOTIKENTTA = "EFHK"        # Helsinki-Vantaa
KENTTIEN_MAARA = 10         # montako kohdekenttaa arvotaan peliin
TAVOITE_RAHA = 400        # paljonko rahaa pitaa kerata voittaakseen
ALKU_POLTTOAINE = 9000     # kilometreina


# ---------------------------------------------------------------
# TIETOKANTA
# ---------------------------------------------------------------

def avaa_yhteys():
    """Avaa yhteyden tietokantaan ja palauttaa yhteysolion."""
    return mysql.connector.connect(**YHTEYS_TIEDOT)


def hae_kentta(yhteys, ident):
    """Hakee yhden lentokentan ICAO-tunnuksen (ident) perusteella."""
    kursori = yhteys.cursor(dictionary=True)
    sql = """SELECT ident, name, municipality, iso_country,
                    latitude_deg, longitude_deg
             FROM airport
             WHERE ident = %s"""
    kursori.execute(sql, (ident,))
    rivi = kursori.fetchone()
    kursori.close()
    return rivi


def arvo_kentat(yhteys, maara, pois_jatettava):
    """Arpoo satunnaisia suuria eurooppalaisia lentokenttia."""
    kursori = yhteys.cursor(dictionary=True)
    sql = """SELECT ident, name, municipality, iso_country,
                    latitude_deg, longitude_deg
             FROM airport
             WHERE type = 'large_airport'
               AND continent = 'EU'
               AND ident <> %s
             ORDER BY RAND()
             LIMIT %s"""
    kursori.execute(sql, (pois_jatettava, maara))
    rivit = kursori.fetchall()
    kursori.close()
    return rivit


# ---------------------------------------------------------------
# APUFUNKTIOT
# ---------------------------------------------------------------

def etaisyys_km(kentta1, kentta2):
    """Laskee kahden kentan valisen etaisyyden kilometreina (haversine)."""
    R = 6371.0
    lat1 = math.radians(float(kentta1["latitude_deg"]))
    lon1 = math.radians(float(kentta1["longitude_deg"]))
    lat2 = math.radians(float(kentta2["latitude_deg"]))
    lon2 = math.radians(float(kentta2["longitude_deg"]))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def nimi(kentta):
    """Muotoilee kentan nimen luettavaan muotoon."""
    return f"{kentta['name']} ({kentta['ident']}), {kentta['municipality']}, {kentta['iso_country']}"


# ---------------------------------------------------------------
# PELI
# ---------------------------------------------------------------

def tulosta_tilanne(pelaaja, sijainti):
    print()
    print("=" * 60)
    print(f"Pelaaja:      {pelaaja['nimi']}")
    print(f"Sijainti:     {nimi(sijainti)}")
    print(f"Rahaa:        {pelaaja['raha']} / {TAVOITE_RAHA}")
    print(f"Polttoaine:   {pelaaja['polttoaine']:.0f} km")
    print("=" * 60)


def tulosta_vaihtoehdot(kohteet, sijainti, kaydyt):
    print("\nMinne lennetaan?")
    for numero, kentta in enumerate(kohteet, start=1):
        matka = etaisyys_km(sijainti, kentta)
        merkki = " [kaytu]" if kentta["ident"] in kaydyt else ""
        print(f"  {numero}. {nimi(kentta)} - {matka:.0f} km{merkki}")
    print("  0. Lopeta peli")


def kysy_valinta(kohteet):
    """Kysyy kayttajalta numeron ja tarkistaa etta se on kelvollinen."""
    while True:
        syote = input("\nValintasi: ").strip()
        if not syote.isdigit():
            print("Anna numero.")
            continue
        valinta = int(syote)
        if 0 <= valinta <= len(kohteet):
            return valinta
        print("Numero ei ole listalla.")


def pelaa():
    yhteys = avaa_yhteys()

    koti = hae_kentta(yhteys, KOTIKENTTA)
    kohteet = arvo_kentat(yhteys, KENTTIEN_MAARA, KOTIKENTTA)

    pelaaja = {
        "nimi": input("Anna nimimerkkisi: ").strip() or "Pilotti",
        "raha": 0,
        "polttoaine": ALKU_POLTTOAINE,
    }

    sijainti = koti
    kaydyt = set()

    print(f"\nTervetuloa! Lahdet kentalta {nimi(koti)}.")
    print(f"Kerää {TAVOITE_RAHA} rahaa ja palaa takaisin kotiin.")

    while True:
        tulosta_tilanne(pelaaja, sijainti)

        # Voittoehto: kotona ja tarpeeksi rahaa
        if sijainti["ident"] == KOTIKENTTA and pelaaja["raha"] >= TAVOITE_RAHA:
            print("\nOnnittelut! Palasit kotiin rahojen kanssa. Voitit pelin!")
            break

        # Naytetaan kohteet + kotikentta
        vaihtoehdot = kohteet + [koti] if sijainti["ident"] != KOTIKENTTA else kohteet
        tulosta_vaihtoehdot(vaihtoehdot, sijainti, kaydyt)

        valinta = kysy_valinta(vaihtoehdot)
        if valinta == 0:
            print("Peli paattyi.")
            break

        kohde = vaihtoehdot[valinta - 1]
        matka = etaisyys_km(sijainti, kohde)

        if matka > pelaaja["polttoaine"]:
            print(f"\nPolttoaine ei riita! Tarvitset {matka:.0f} km, sinulla on {pelaaja['polttoaine']:.0f} km.")
            continue

        pelaaja["polttoaine"] -= matka
        sijainti = kohde
        print(f"\nLensit {matka:.0f} km kentalle {nimi(kohde)}.")

        # Rahan kerays: vain ensimmaisella kaynnilla
        if kohde["ident"] not in kaydyt and kohde["ident"] != KOTIKENTTA:
            kaydyt.add(kohde["ident"])
            loyto = random.randint(50, 150)
            pelaaja["raha"] += loyto
            print(f"Loysit {loyto} rahaa!")

        if pelaaja["polttoaine"] <= 0:
            print("\nPolttoaine loppui. Peli paattyi.")
            break

    yhteys.close()


if __name__ == "__main__":
    pelaa()