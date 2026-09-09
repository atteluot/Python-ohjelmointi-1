Vuoden_ajat = {
    12: "talvi", 1: "talvi", 2: "talvi",
    3: "kevät", 4: "kevät", 5: "kevät",
    6: "kesä", 7: "kesä", 8: "kesä",
    9: "syksy", 10: "syksy", 11: "syksy"
}
kuukausi = int(input("Anna kuukauden nunero (1-12):"))
vuodenaika = Vuoden_ajat.get(kuukausi)
if vuodenaika:
    print(f"Kuukautta {kuukausi} vastaava vuodenaika on {vuodenaika}.")
else:
    print("Virhe anna numero väliltä 1-12.")
