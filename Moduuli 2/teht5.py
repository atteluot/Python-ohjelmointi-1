try:
    leiviskät = float(input("Anna leiviskät:"))
    naulat = float(input("Anna naulat:"))
    luodit = float(input("Anna luodit:"))
except ValueError:
    print("Anna luku.")
else:
    luoti = 0.0133
    naula = luoti * 32
    leiviskä = naula * 20

    luotien_paino = luodit * luoti
    naulojen_paino = naulat * naula
    leiviskien_paino = leiviskät * leiviskä

    massa1 = luotien_paino + naulojen_paino + leiviskien_paino
    massa2 = round(massa1 * 1000)
    k = massa2 // 1000
    g = massa2 % 1000
    print(f"Massa nykymittojen mukaan: {k} Kiloa ja {g} Grammaa.")
