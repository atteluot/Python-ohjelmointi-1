try:
    päivät = float(input("Anna päivät:"))
except ValueError:
    print("Anna luku.")
else:
    sekuntti = 86400
    print(round(päivät * sekuntti, 2))
