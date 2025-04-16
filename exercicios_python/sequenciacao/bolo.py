import math

def max_bolos(A, B, C):

    qtd_farinha = A // 2
    qtd_ovos = B // 3
    qtd_leite = C // 5

    qtd_bolos = min(qtd_farinha, qtd_ovos, qtd_leite)

    return qtd_bolos

A, B, C = [int(w) for w in input("Digite a quantidade de xícaras de farinha, ovos e colheres de sopa de leite separadas por espaço: ").split()]

print(max_bolos(A, B, C))