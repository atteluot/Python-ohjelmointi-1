import math
def hintaneliönä(halkaisia,hinta):
    halkaisiam = halkaisia / 100

    säde = halkaisia / 2
    pintaala = math.pi * (säde**2)
    hinta_neliö = hinta / pintaala
    return hinta_neliö
print("---------------------------------------")
print("---Ensimmäinen pizza---")
halkaisia = float(input("Anna pizzan halkaisia (cm):"))
hinta = float(input("Anna pizzan hinta (€):"))
tulos1 = hintaneliönä(halkaisia, hinta)
print(f"Pizza 2 neliömetrihinta on: {tulos1} €/m²")
print("---------------------------------------")
print("---Toinen pizza---")
halkaisia = float(input("Anna pizzan halkaisia (cm):"))
hinta = float(input("Anna pizzan hinta (€):"))
tulos2 = hintaneliönä(halkaisia, hinta)
print(f"Pizza 1 neliömetrihinta on: {tulos2} €/m²")
print("---------------------------------------")
if tulos1 < tulos2:
    print("Pizza 1 on parempi vastike rahalle.")
elif tulos2 < tulos1:
    print("Pizza 2 on parempi vastike rahalle")
print("---------------------------------------")