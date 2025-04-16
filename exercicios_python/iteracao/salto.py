import math

qtd = int(input())
maior_salto = -math.inf

for _ in range (qtd):
    maior_salto_ind = -math.inf
    s1, s2, s3, nome = [(w) for w in input().split()]
    
    maior_salto_ind = max(float(s1), float(s2), float(s3))
    
    if maior_salto_ind > maior_salto:
        melhor_atleta = nome
        maior_salto = maior_salto_ind
        
print(melhor_atleta)
    

