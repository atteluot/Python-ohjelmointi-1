

import mysql.connector


def hae_kentta(yhteys, ident):
    #Hakee yhden lentokentan ICAO-tunnuksen perusteella.
    kursori = yhteys.cursor(dictionary=True)
    sql = """SELECT ident, name, municipality, iso_country,
                    latitude_deg, longitude_deg
             FROM airport
             WHERE ident = %s"""
    kursori.execute(sql, (ident,))
    rivi = kursori.fetchone()
    kursori.close()
    return rivi

# ---------------------------------------------------------------
# TESTI
# ---------------------------------------------------------------

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="atte",
    password="140507"
)

# Testi 1: tunnus joka pitäisi löytyä
tulos = hae_kentta(yhteys, "EDDF")

print(tulos)
print()



yhteys.close()