kuha = float(input("Anna kuhan mitta:"))
if kuha < 37.0 :
    print("Kuha on alimittainen laske takaisin vesistöön.")
    puuttuu = 37 - kuha
    print("Kuhan pituutta puuttuu", puuttuu)
elif kuha >= 37.0:
    print("Kuha on oikean mittainen")
