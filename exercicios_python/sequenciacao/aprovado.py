import math

media = 6

nota_1 = float(input("Digite o valor da primeira nota: "))
nota_2 = float(input("Digite o valor da segunda nota: "))
nota_3 = float(input("Digite o valor da terceira nota: "))

peso_1 = float(input("Digite o peso da primeira nota: "))
peso_2 = float(input("Digite o peso da segunda nota: "))
peso_3 = float(input("Digite o peso da terceira nota: "))

media_final = ((nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3)) / (peso_1 + peso_2 + peso_3)

print(media_final >= media)