lukulista=[]
while True:
    syötä=int(input("Anna Lukuja (0 lopettaa):"))
    if syötä == 0:
        break
    else:
        lukulista.append(syötä)

def parittomat(lukulista):
    parilliset = [
    
    ]
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    for luku in list(parilliset):
        lukulista.remove(luku)
    return parilliset

print("Tässä parittomat", parittomat(lukulista))