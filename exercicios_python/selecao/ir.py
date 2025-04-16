salario_bruto = float(input())
num_dependentes = int(input())
desc_dependente = 137.99

if salario_bruto > 1372.81:
    if 1372.82 <= salario_bruto <= 2743.25:
        aliquota = 0.15
        deducao = 205.92
    else:
        aliquota = 0.275
        deducao = 548.82

    if salario_bruto <= 720:
        inss = (salario_bruto * 0.0765)
    elif 720 < salario_bruto <= 1200:
        inss = (salario_bruto * 0.09)
    elif 1200 < salario_bruto <= 2400:
        inss = (salario_bruto * 0.11)
    else:
        inss = 2400 * 0.11

    # calculo irrf
    irrf = (salario_bruto - (num_dependentes * desc_dependente) - inss) * aliquota - deducao

else:
    # isenção irrf
    irrf = 0.00


print(f'{irrf:.2f}')

