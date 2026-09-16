import mysql.connector

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='atte',
         password='140507',
         autocommit=True
         )

cursor = yhteys.cursor()

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""

cursor.execute(sql, (icao,))
tulos = cursor.fetchone()

if tulos:
    print(f"Lentoasema: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentoasemaa ei löytynyt.")

cursor.close()
yhteys.close()