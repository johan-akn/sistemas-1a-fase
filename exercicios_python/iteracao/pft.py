
def ehPerfeito(num):
    somaDiv = 0
    
    for i in range (num, 1, 1):
        if num % i == 0:
            somaDiv += i
        else:
            break
    if somaDiv == num:
        resultado = f'{num} eh perfeito'
    else:
        resultado = f'{num} nao eh perfeito'
        
    return resultado
        
qtd = int(input())

for _ in range(qtd):
    num = int(input())
    ehPerfeito(num)