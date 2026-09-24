import random
import os

# Määritellään korttien maat ja arvot
MAAT = ['Hertta', 'Ruutu', 'Risti', 'Pata']
ARVOT = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def tyhjenna_ruutu():
    """Tyhjentää terminaalin ruudun käyttöjärjestelmästä riippuen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def luo_pakka():
    """Luo ja sekoittaa 52 kortin pakan."""
    pakka = [f"{arvo} {maa}" for maa in MAAT for arvo in ARVOT]
    random.shuffle(pakka)
    return pakka

def kortin_arvo(kortti):
    """Palauttaa yksittäisen kortin numeroarvon."""
    arvo_str = kortti.split()[0]
    if arvo_str in ['J', 'Q', 'K']:
        return 10
    elif arvo_str == 'A':
        return 11
    else:
        return int(arvo_str)

def laske_kaden_arvo(kasi):
    """Laskee käden kokonaisarvon ja huomioi Ässän (1 tai 11)."""
    arvo = sum(kortin_arvo(k) for k in kasi)
    assat = sum(1 for k in kasi if k.split()[0] == 'A')
    
    # Jos arvo menee yli 21 ja kädessä on ässiä, muutetaan ässien arvo 11 -> 1
    while arvo > 21 and assat > 0:
        arvo -= 10
        assat -= 1
        
    return arvo

def tulosta_poyta(pelaajan_kasi, jakajan_kasi, peli_ohi=False):
    """Tulostaa pelitilanteen ruudulle."""
    tyhjenna_ruutu()
    print("=" * 30)
    print("          BLACKJACK")
    print("=" * 30 + "\n")
    
    print("JAKAJAN KÄSI:")
    if not peli_ohi:
        print(f"  [Piilotettu kortti]")
        print(f"  {jakajan_kasi[1]}")
    else:
        for kortti in jakajan_kasi:
            print(f"  {kortti}")
        print(f"  (Arvo: {laske_kaden_arvo(jakajan_kasi)})\n")
        
    print("\nPELAAJAN KÄSI:")
    for kortti in pelaajan_kasi:
        print(f"  {kortti}")
    print(f"  (Arvo: {laske_kaden_arvo(pelaajan_kasi)})\n")
    print("-" * 30)

def pelaa():
    pakka = luo_pakka()
    
    # Jaetaan kaksi ensimmäistä korttia
    pelaajan_kasi = [pakka.pop(), pakka.pop()]
    jakajan_kasi = [pakka.pop(), pakka.pop()]
    
    # Tarkistetaan suora Blackjack
    pelaajan_arvo = laske_kaden_arvo(pelaajan_kasi)
    if pelaajan_arvo == 21:
        tulosta_poyta(pelaajan_kasi, jakajan_kasi, peli_ohi=True)
        print("BLACKJACK! Voitit!\n")
        return

    # Pelaajan vuoro
    while True:
        tulosta_poyta(pelaajan_kasi, jakajan_kasi)
        pelaajan_arvo = laske_kaden_arvo(pelaajan_kasi)
        
        if pelaajan_arvo > 21:
            tulosta_poyta(pelaajan_kasi, jakajan_kasi, peli_ohi=True)
            print("Menit yli 21. HÄVISIT!\n")
            return
            
        valinta = input("Haluatko lisää kortteja? (h = hit / s = stand): ").lower().strip()
        if valinta == 'h':
            pelaajan_kasi.append(pakka.pop())
        elif valinta == 's':
            break

    # Jakajan vuoro
    while laske_kaden_arvo(jakajan_kasi) < 17:
        jakajan_kasi.append(pakka.pop())
        
    jakajan_arvo = laske_kaden_arvo(jakajan_kasi)
    tulosta_poyta(pelaajan_kasi, jakajan_kasi, peli_ohi=True)
    
    # Voittajan selvitys
    if jakajan_arvo > 21:
        print("Jakaja meni yli! VOITIT!\n")
    elif jakajan_arvo > pelaajan_arvo:
        print("Jakajalla on suurempi arvo. HÄVISIT!\n")
    elif jakajan_arvo < pelaajan_arvo:
        print("Sinulla on suurempi arvo. VOITIT!\n")
    else:
        print("Tasapeli (Push). SAAT PANOKSEN TAKAISIN!\n")

def main():
    while True:
        pelaa()
        uudestaan = input("Pelataanko uudestaan? (k = kyllä / e = ei): ").lower().strip()
        if uudestaan != 'k':
            print("\nKiitos peleistä! Nähdään taas.")
            break

if __name__ == "__main__":
    main()