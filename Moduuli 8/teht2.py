import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="atte",
    password="****", #salasana vaihdettu 
    database="flight_game"
)

cursor = yhteys.cursor()

maakoodi = input("Anna maa koodi:")
sql = """
    SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"""
cursor.execute(sql, (maakoodi,))
tulo = cursor.fetchall(

)
for rivi in tulo:
    print(rivi[0],rivi[1])

cursor.close()
yhteys.close()