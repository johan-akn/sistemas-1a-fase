import math

salario_base = 2500
hora_base = 200
salario_hora = salario_base / hora_base
salario_hora_extra = salario_hora + (salario_hora * 20/100)
taxa_inss = 9/100
taxa_ir = 13/100

horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))

salario_bruto = (horas_trabalhadas * salario_hora) + (horas_extras * salario_hora_extra)
valor_ir = salario_bruto * taxa_ir
valor_inss = salario_bruto * taxa_inss
salario_liquido = salario_bruto - (valor_ir + valor_inss)

print(f"- Salário Bruto: {salario_bruto:.2f}")
print(f"- IR: {valor_ir:.2f}")
print(f"- INSS: {valor_inss:.2f}")
print(f"- Salário Líquido: {salario_liquido:.2f}")