try:
    kanta = float(input("Anna suorakulmion kanta:"))
    Korkeus = float(input("Anna suorakulmion korkeus:"))
except ValueError:
    print("Anna luku.")
else:
    pintaala = kanta*Korkeus
    piiri = (2 * kanta) + (2 * Korkeus)
    print("Pintaala on:", round(pintaala, 2))
    print("Piiri on:", round(piiri, 2))
