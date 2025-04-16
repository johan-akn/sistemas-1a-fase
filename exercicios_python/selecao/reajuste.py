salario = float(input())
salario_min = float(input())

qtd_salarios_min = salario / salario_min
salario_final = salario

if qtd_salarios_min <= 3:
    salario_final = salario + (salario * 0.2)
elif 3 < qtd_salarios_min <= 5:
    salario_final = salario + (salario * 0.15)
else:
    salario_final = salario + (salario * 0.1)

if salario_final < salario_min * 1.5:
    salario_final = salario_min * 1.5
elif salario_final > salario_min * 20:
    salario_final = salario_min * 20

print(f'{salario_final:.2f}')