comprimento = float(input())
largura = float(input())
gavetas = int(input())
tipo = str(input())

preco_min = 200
area = comprimento * largura

if area > 2:
    acrescimo_area = 50.00
else:
    acrescimo_area = 0.00

if tipo == 'mogno':
    valor_madeira = 150.00
elif tipo == 'carvalho':
    valor_madeira = 125.00
else: 
    valor_madeira = 0.00

valor = max(preco_min, valor_madeira + acrescimo_area + (area * 100) + (gavetas * 30.00))


print(f'{valor:.2f}')