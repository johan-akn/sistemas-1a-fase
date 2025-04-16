valor_produto = float(input())
desc_1 = 0.2
desc_2 = 0.1
desc_3 = 0.15


if 500 <= valor_produto <= 1000:
    valor_final = valor_produto - (valor_produto * (desc_1 + desc_2))
elif valor_produto > 1000:
    sobra_valor = valor_produto - 1000
    valor_final = sobra_valor - (sobra_valor * (desc_1 + desc_2 + desc_3)) + (1000 - (1000 * (desc_1 + desc_2)))
else:
    valor_final = valor_produto - (valor_produto * desc_1)

print(f'{valor_final:.2f}')