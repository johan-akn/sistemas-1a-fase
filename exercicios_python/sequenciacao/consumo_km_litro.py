import math

distancia_percorrida = int(input("Digite a distância percorrida (km): "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto: "))

consumo = distancia_percorrida / combustivel_gasto

print("Gasto: ", f"{consumo:.3f}", "km/l." )