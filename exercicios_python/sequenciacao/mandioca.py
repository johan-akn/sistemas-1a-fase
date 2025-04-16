import math

porcao_curupira = 300
porcao_boitata = 1500
porcao_boto = 600
porcao_mapinguari = 1000
porcao_lara = 150
porcao_chica = 225

A, B, C, D, E = [int(w) for w in input("Digite a quantidade de porções de cada um dos cinco convidados separadas por espaço: ").split()]

qtd_mandioca = (porcao_curupira * A) + (porcao_boitata * B) + (porcao_boto * C) + (porcao_mapinguari * D) + (porcao_lara * E) + porcao_chica

print(f"\n Quantidade de mandioca necessária: {qtd_mandioca} gramas.")