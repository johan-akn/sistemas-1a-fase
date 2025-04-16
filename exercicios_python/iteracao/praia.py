import math

def processar_praias(qtd):
    soma_dist = 0
    qtd_exc = 0
    maior_dist = -math.inf
    nome_maior_dist = ""

    for _ in range(qtd):
        praia, distancia = input().split(';')
        distancia = int(distancia)

        if distancia > maior_dist:
            maior_dist = distancia
            nome_maior_dist = praia

        if 15 <= distancia <= 20:
            qtd_exc += 1

        soma_dist += distancia

    media_dist = soma_dist / qtd
    return nome_maior_dist, qtd_exc, media_dist


qtd = int(input())
nome_maior_dist, qtd_exc, media_dist = processar_praias(qtd)
print(f'{nome_maior_dist};{qtd_exc};{media_dist:.1f}')
