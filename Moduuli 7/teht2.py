niemt = set()
print("Anna nimiä. Tyhjä lopettaa.")
while True:
    nimi = input("Anna nimi:")
    if nimi == "":
        print("ohjelma loppuu:")
        print("Tässä nimet.")
        for n in niemt:
            print(n)
        break
    elif nimi in niemt:
        print("Ajemmin syötetty nimi")
    else:
        niemt.add(nimi)
        print("Uusi nimi")
