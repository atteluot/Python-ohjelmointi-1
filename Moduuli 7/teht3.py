lentoasemat = {}
while True:
    print("Valitse toiminto")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Syötä numero: ")

    if valinta == "1":
        print("Lisää lentoasema")
        icao = input("Syötä lentoaseman ICAO-Koodi:")
        lentonimi = input("Anna lentoaseman nimi:")
        if icao != "" and lentonimi != "":
            lentoasemat[icao] = lentonimi
            print("Tallennetu")
        else:
            print("VIRHE!")

    elif valinta == "4321":
        print("-------------------------")
        print("Löysit easter egg:in")
        print("---------------------------")

    elif valinta == "2":
        print("Etsi lentoasema")
        etsi = input("Anna lentoaseman ICAO-Koodi:")
        if etsi in lentoasemat:
            print(f"ICAO-Koodia {etsi} vastaava lentoasema on: {lentoasemat[etsi]}")
        else:
            print("ICAO-Koodia vastaavaa lentoasemaa ei löytynty")
            
    elif valinta == "3":
        print("Ohjelma loppuu.")
        break
    else:
        print("Virheellinen valinta")