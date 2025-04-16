import math

# Entrada de dados
nota_a = float(input("Digite a primeira nota: "))
nota_b = float(input("Digite a segunda nota: "))
nota_c = float(input("Digite a terceira nota: "))

# Definição dos pesos
peso_a = 2
peso_b = 3
peso_c = 5

# Cálculo da média
media = ((nota_a * peso_a) + (nota_b * peso_b) + (nota_c * peso_c)) / (peso_a + peso_b + peso_c)

# Saída de dados
print(f"MÉDIA = {media:.1f}")