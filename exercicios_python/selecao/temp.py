origem = input().lower()
temp_origem = float(input())
destino = input().lower()

match origem:
    case 'k':
        celsius = temp_origem - 273.15
    case 'f':
        celsius = (temp_origem - 32) * 5/9
    case 'r':
        celsius = (temp_origem - 491.67) * 5/9
    case 'c':
        celsius = temp_origem
    case _:
        print('Unidade de origem inválida.')
        exit()
        
match destino:
    case 'k':
        temp_final = celsius + 273.15
    case 'f':
        temp_final = (celsius * 9/5) + 32
    case 'r':
        temp_final = (celsius + 273.15) * 9/5
    case 'c':
        temp_final = celsius
    case _:
        print('Unidade de destino inválida.')
        exit()
        
print(temp_final)
    
    