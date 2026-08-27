import random
kuuti = int(input("Anna arpakuutioiden määrä:"))
luvutlista = []
for i in range(kuuti):
    luvut = random.randint(1,6)
    luvutlista.append(luvut)
print(luvutlista)
summa = sum(luvutlista)
print(f"Random lukujen summa on {summa}.")