try:
    grammat = int(input("Anna grammat:"))
except ValueError:
    print("Anna kokonaisluku.")
else:
    if grammat < 0:
        print("Anna positiivinen luku.")
    else:
        k = grammat // 1000
        g = grammat % 1000
        print("Määrä kilona ja grammoina",k,"kg",g,"g")
