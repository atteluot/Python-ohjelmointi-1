lista = []
while True:
    syöte = (input("Anna numero:"))
    
    
    if syöte == "":
        
            pienin = min(lista)
            isoin = max(lista)

            print(f"Loppu pienin oli {pienin} Isoin oli {isoin}.")
            break
    else:
        numero = int(syöte)
        lista.append(numero)
        