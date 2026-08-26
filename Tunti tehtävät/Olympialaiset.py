v = int(input("Anna Vuosi:"))
if v % 4 == 0 and v != 2020:
    print("Oli Olympia vuosi")
elif v == 2021:
    print("Oli poikkeuksellisesti Olympia vuosi")
elif v == 2020:
    print("Ei ollut Olympia vuosi")
else:
    print("Ei ollut Olympia vuosi")