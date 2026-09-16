import mysql.connector
from geopy.distance import geodesic
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="atte",
    password="sdsda", #salasana vaihdettu 
    database="flight_game"
)

cursor = yhteys.cursor()


icao1 = input("Anna ensimmäisen kentän ICAO-koodi:")
icao2 = input("Anna toisen kentän ICAO-koodi:")
#EGLL
#EFHK
def eka(icao):
    sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao1,))
    rivi1 = cursor.fetchall()       
    return rivi1
def toka(icao):
    sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao2,))
    rivi2 = cursor.fetchall()
    return rivi2

tulos1 = eka(icao1)
tulos2 = toka(icao2)
print(F"Lentokentät {tulos1} ja {tulos2}")


if tulos1 and tulos2:
    
    piste1 = (tulos1[0][1], tulos1[0][2])
    piste2 = (tulos2[0][1], tulos2[0][2])
    
    etaisyys = geodesic(piste1, piste2).kilometers
    print(f"Etäisyys on: {etaisyys:.1f} km")