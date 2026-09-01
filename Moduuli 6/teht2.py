import random
def noppa():
    tahkot = int(input("Anna tahkojen määrä:"))
    while True:
        vastaus = random.randint(1,tahkot)
        print(vastaus)
        if vastaus == tahkot:
            break
noppa() 
            