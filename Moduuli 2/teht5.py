leiviskät = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

luoti = 0.0133
naula = luoti * 32
leiviskä = naula * 20

luotien_paino = luodit * luoti
naulojen_paino = naulat * naula
leivisköjen_paino = leiviskät * leiviskä

massa1 = luotien_paino + naulojen_paino + leivisköjen_paino
massa2 = int(massa1 * 1000)
k = int(massa2 // 1000)
g = massa2 % 1000
print("Massa nykymittojen mukaan:",k,"Kiloa ja",g,"Grammaa.")