pituus = int(input("Anna pituutesi:"))
if pituus < 100:
    print("Et pääse laitteisiin.")
elif pituus >= 100 and pituus <= 139:
    print("Pääset lasten laitteisiin.")
elif pituus >= 195:
    print("et pääse kirnuun, muuta pääset muihin laitteisiin.")
elif pituus >= 140 and pituus <= 194:
    ikä = int(input("Anna ikäsi:"))
    if ikä < 8:
        print("Et pääse Tulirekeen mutta pääset muihin laitteisiin.")
    else:
        print("Pääset kaikkiin laitteisiin.")

 