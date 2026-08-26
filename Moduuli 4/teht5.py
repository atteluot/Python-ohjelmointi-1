oikeasala = "rules"
oikeatunnus = "python"
yritykset = 0

while True:
    ktunnus = input("Anna tunnuksesi:")
    sala = input("Anna salasanasi:")

    if sala != oikeasala or ktunnus != oikeatunnus:
        print("Pääsy evätty")
        yritykset += 1
        if yritykset == 5:
            print("Liikaa vääriä")
            break
                 
    elif sala == oikeasala and ktunnus == oikeatunnus:
        print("Tervetuloa!")
        break
    
        