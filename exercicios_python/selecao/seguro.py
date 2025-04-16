valor_veiculo = float(input())
classe_desc = str(input())
proc_veiculo = str(input())
idade = int(input())

if(proc_veiculo == 'nacional'):
    valor_base = valor_veiculo*0.1
elif(proc_veiculo == 'estrangeira'):
    valor_base = valor_veiculo*0.15

valor_premio = valor_base

match classe_desc:
    case classe_desc if classe_desc == 'A':
        valor_premio -= valor_base*0.3
    case classe_desc if classe_desc == 'B':
        valor_premio -= valor_base*0.2
    case classe_desc if classe_desc == 'C':
        valor_premio -= valor_base*0.1
    case classe_desc if classe_desc == 'D':
        valor_premio -= valor_base*0.05
    case classe_desc if classe_desc == 'E':
        valor_premio = valor_base*1
    case _:
        print('Classe inválida.')

if(idade > 24):
    valor_premio -= valor_base*0.1


print(f'{valor_premio:.2f}')