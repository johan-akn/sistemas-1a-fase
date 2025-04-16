import math

conteudo_galao = 3.6
valor_galao = 25
capacidade_galao = 18 * conteudo_galao

area = int(input("Digite a área a ser pintada: "))

qtd_galoes = max(1, round(area / capacidade_galao))
valor_final = qtd_galoes * valor_galao

print("Área de cobertura: ", area)
print("Número de galões: ", qtd_galoes)
print("Valor a ser pago: R$", valor_final)