a = float(input())
b = float(input())
c = float(input())

media = round((a+b+c) / 3, 1)

match media:
    case media if 9 <= media <= 10:
        print('Ótimo')
    case media if 7.5 <= media < 9:
        print('Bom')
    case media if 6.0 <= media < 7.5:
        print('Satisfatório')
    case media if 0.0 <= media < 6:
        print('Insuficiente')
    case _:
        print('Média inválida')