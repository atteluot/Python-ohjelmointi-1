#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
#onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
v = int(input("Anna vuosi luku:"))
if (v % 4 == 0 and v % 100 != 0) or (v % 400 == 0):
    print(f"Vuosi {v} on karkaus vuosi.")
else: 
    print(F"Vuosi {v} ei ole karakus vuosi")