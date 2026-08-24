try:
    numero1 = int(input("Anna ensimmäinen kokonaisluku:"))
    numero2 = int(input("Anna toinen kokonaisluku:"))
    numero3 = int(input("Anna kolmas kokonaisluku:"))
except ValueError:
    print("Anna kokonaisluku.")
else:
    summa = numero1 + numero2 + numero3
    tulo = numero1 * numero3 * numero2
    keskiarvo = summa / 3

    print(summa)
    print(tulo)
    print(round(keskiarvo, 2))
