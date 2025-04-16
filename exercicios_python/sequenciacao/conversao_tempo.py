import math

num = int(input("Digite o tempo em segundos: "))

horas = num // 3600
resto = num % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")