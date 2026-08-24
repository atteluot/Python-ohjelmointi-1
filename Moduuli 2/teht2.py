import math

try:
    säde = float(input("Anna ympyrän säde:"))
except ValueError:
    print("Anna luku.")
else:
    pintaala = (säde ** 2) * math.pi
    print("pintaala on:",round(pintaala, 2))
