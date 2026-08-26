import random
noppa = random.randint(1,10)
while True:
    arvaus = int(input("Arvaa kokonais luku (1-10):"))
    if arvaus > noppa:
        print("Liian iso arvaus!")
    elif arvaus < noppa:
        print("Liian Pieni arvaus!")
    else: 
        print("Arvasit oikein!")
        break
