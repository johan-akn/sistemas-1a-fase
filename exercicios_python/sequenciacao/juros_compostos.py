import math

capital = float(input("Digite o valor do capital: "))
num_meses = int(input("Digite o número de meses: "))
taxa = float(input("Digite o valor da taxa (%): "))

for i in range(num_meses):
    capital += capital * (taxa/100)

valor_final = round(capital, 2)

print("Valor final após ", num_meses, "meses com taxa de ", taxa, "%: R$", valor_final)