raha = 10
import random
print("-------Kolikon heitto-------")
print("Kuinka paljon haluat betata.")
print("A= 1€")
print("B= 2€")
print("C= 5€")
bet = input("Anna betti (A,B,C): ")
valinta = input("Kruuna vai klaava: ")
if raha == 0:
    print("Hävisit rahat loppui.")

elif bet == "A":
    vastaus= random.randint(1,2)
    if vastaus == 1 and valinta == "Kruuna":
        raha = raha + 1 
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    elif vastaus == 2 and valinta == "Klaava":
        raha = raha + 1 
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    else:
        raha = raha -1 
        print(F"Hävisit salostasi miinustetaan 1€ rahasi on{raha}€")
elif bet == "B":
    vastaus= random.randint(1,2)
    if vastaus == 1 and valinta == "Kruuna":
        raha = raha + 2
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    elif vastaus == 2 and valinta == "Klaava":
        raha = raha + 2
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    else:
        raha = raha - 2 
        print(F"Hävisit salostasi miinustetaan 2€ rahasi on {raha}€")
elif bet == "C":
    vastaus= random.randint(1,2)
    if vastaus == 1 and valinta == "Kruuna":
        raha = raha + 5
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    elif vastaus == 2 and valinta == "Klaava":
        raha = raha + 5
        print(f"Voitit saldoosi lisättiin voitto {raha}€")
    else:
        raha = raha - 5 
        print(F"Hävisit salostasi miinustetaan 5€ rahasi on{raha}€")
