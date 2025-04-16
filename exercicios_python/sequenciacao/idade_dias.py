import math

num_dias = int(input("Digite a idade em dias: "))

anos = num_dias // 365
resto = num_dias % 365
meses = resto // 30
dias = resto % 30

print(f"{anos} ano (s) \n {meses} mes (es) \n {dias} dia (s)")