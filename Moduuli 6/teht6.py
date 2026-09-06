import math
def hintaneliönä(halkaisia,hinta):
    halkaisiam = halkaisia / 100

    säde = halkaisia / 2
    pintaala = math.pi * (säde**2)
    hinta_neliö = hinta / pintaala
    return hinta_neliö

print("Ensimmäinen pizza")
halkaisia = float(input("Anna pizzan halkaisia (cm):"))
hinta = float(input("Anna pizzan hinta (€):"))
tulos = hintaneliönä(halkaisia, hinta)
print(f"Pizzan neliömetrihinta on: {tulos} €/m²")