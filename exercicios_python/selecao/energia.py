gasto = int(input())

taxa_1 = 0.09556
taxa_2 = 0.16698
taxa_3 = 0.25052
taxa_4 = 0.27836

if 0 < gasto <= 30:
    valor_conta = gasto * taxa_1
elif 31 <= gasto <= 100:
    valor_conta = (30 * taxa_1) + ((gasto - 30) * taxa_2)
elif 101<= gasto <= 200:
    valor_conta = (30 * taxa_1) + (70 * taxa_2) + ((gasto - 100) * taxa_3)
elif gasto > 200:
    valor_conta = (30 * taxa_1) + (70 * taxa_2) + (100 * taxa_3) + ((gasto - 200) * taxa_4)
else:
    valor_conta = 0

print(f'{valor_conta:.2f}')