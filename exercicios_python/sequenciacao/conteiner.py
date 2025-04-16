def maximo_conteiner(A,B,C,X,Y,Z):
    conteiner_por_largura = X // A
    conteiner_por_comprimento = Y // B
    conteiner_por_altura = Z // C

    total_conteiners = conteiner_por_largura * conteiner_por_comprimento * conteiner_por_altura

    return total_conteiners

A, B, C = [int(w) for w in input("Digite as dimensões dos contêineres divididas por espaço: ").split()]
X, Y, Z = [int(w) for w in input("Digite as dimensões do barco divididas por espaço: ").split()]

print(maximo_conteiner(A,B,C,X,Y,Z))