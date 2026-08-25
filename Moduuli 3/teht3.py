sukupuoli = input("Anna sukupuolesi (Nainen/Mies):")
hemoglobiini = int(input("Anna hemoglobiini arvosi (g/l):"))

if sukupuoli == "Nainen" and hemoglobiini < 117:
    print("hemoglobiiniarvo alhainen")
elif sukupuoli == "Nainen" and 117 <= hemoglobiini <= 175:
    print("hemoglobiiniarvo normaali")
elif sukupuoli == "Nainen" and hemoglobiini > 175:
    print("hemoglobiiniarvo korkea")
elif sukupuoli == "Mies" and hemoglobiini < 134:
    print("hemoglobiiniarvo alhainen")
elif sukupuoli == "Mies" and 134 <= hemoglobiini <= 195:
    print("hemoglobiiniarvo normaali")
elif sukupuoli == "Mies" and hemoglobiini > 195:
    print("hemoglobiiniarvo korkea")