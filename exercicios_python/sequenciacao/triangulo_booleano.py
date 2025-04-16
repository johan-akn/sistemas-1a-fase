import math

a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

def forma_triangulo(a, b, c):
    return (a+b>c) and (a+c>b) and (b+c>a)

print("É um triângulo?", forma_triangulo(a, b, c))