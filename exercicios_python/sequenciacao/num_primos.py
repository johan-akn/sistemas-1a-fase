import math

n = float(input("Digite o valor de n: "))

P = round(n / math.log(n), 1)
M = round(1.25506 * (n / math.log(n)), 1)

print(f"{P} {M}")