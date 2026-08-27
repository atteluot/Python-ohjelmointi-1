
luku = int(input("Anna kokonaisluku: "))

jako = 0

for i in range(1, luku ):
    if luku % i == 0:
        jako += 1  

if jako == 1:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

