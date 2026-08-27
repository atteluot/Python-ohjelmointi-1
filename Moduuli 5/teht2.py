lista = []
while True:
    syöte = (input("Anna numero:"))
    if syöte == "" :
        break
    else:
        numero = int(syöte)
        lista.append(numero)
lista.sort(reverse=True)
print(lista)
for ekat in lista[:5]:
    print(ekat)