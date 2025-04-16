import math

L, D = [float(w) for w in input("Digite o tamanho da estrada e a distância entre os pedágios separados por espaço: ").split()]
K, P = [float(w) for w in input("Digite o custo por km e o preço dos pedágios separados por espaço: ").split()]


qtd_pedagios = L // D
gasto_pedagio = qtd_pedagios * P
gasto_km = L * K
valor_final = gasto_pedagio + gasto_km

print(f"Valor final: R${valor_final}")