import os
import shutil

# Etsitään peli.py yleisistä latauspaikoista
etsittavat_polut = [
    os.path.expanduser("~/Downloads/peli.py"),
    os.path.expanduser("~/Desktop/peli.py"),
    os.path.expanduser("~/Työpöytä/peli.py")
]

kohde = "peli.py"
loytyi = False

for polku in etsittavat_polut:
    if os.path.exists(polku):
        shutil.copy(polku, kohde)
        print(f"✅ Onnistui! Tiedosto löytyi ja kopioitiin kansiosta: {polku}")
        print("Voit nyt käynnistää pelin komennolla: python peli.py")
        loytyi = True
        break

if not loytyi:
    print("❌ Tiedostoa peli.py ei löytynyt Latauksista tai Työpöydältä.")
    print("Varmista, että olet tallentanut pelikoodin nimellä 'peli.py' jompaan kumpaan näistä kansioista.")