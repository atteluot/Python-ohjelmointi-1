autotiedot= {"merkki" : "toyota", "vm": "2000"}

print(autotiedot["merkki"])




    
print("---------------------------------------------------------------")
luvut = []
while True:
    lisäys = int(input("Anna lukuja 0 lopettaa:"))
    
    if lisäys == 0:
        summa = sum(luvut)
        määrä = len(luvut)
        kesk = summa / määrä
        print(kesk)
        break
    luvut.append(lisäys)