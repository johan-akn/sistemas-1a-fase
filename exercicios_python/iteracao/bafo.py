def calcBafo(x):
    ganhador = ''
    somaA = 0
    somaB = 0
    
    for _ in range (x):
        a, b = [int(w) for w in input().split()]
        somaA += a
        somaB += b
            
    if somaA > somaB:
        ganhador = 'Aldo'
    elif somaA < somaB:
        ganhador = 'Beto'
    
    return print(f'Teste {n}\n{ganhador}\n')
    
n = 0
while True:
    x = int(input())
    n += 1
    
    if x == 0:
        break
    else:
        calcBafo(x)