#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
#  kunnes käyttäjä antaa negatiivisen tuumamäärän.
#  Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
tuuma = 2.54

while True:
    tuumamäärä = int(input("Anna tuuma määrä:"))
    cm = tuuma * tuumamäärä

    if tuumamäärä >= 0:
            print(cm,"cm")
    else:
          print("Ohejelma loppuu.")
          break
          
