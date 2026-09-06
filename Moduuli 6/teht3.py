
def lasku():
    maara = float(input("Anna galloneiden määrä: "))
    litra = maara * 3.7
    if maara < 0:
        print("Ohjelma loppuu.")
    elif maara >= 0:
        print(f"{maara} galloonaa on litroina {litra} Litraa.")

lasku()
