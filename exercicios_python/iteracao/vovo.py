import math

n, s = [int(w) for w in input().split()]
menorValor = math.inf

def calcVovo(n):
    for _ in range (n):
        v = int(input())
        s += v
        if v < menorValor:
            menorValor = v
    return menorValor

print(calcVovo(n))