materia_1 = str(input()).upper()
materia_2 = str(input()).upper()
materia_3 = str(input()).upper()
materia_4 = str(input()).upper()

if materia_1 == 'A':
    nota_1 = 4
elif materia_1 == 'B':
    nota_1 = 3
elif materia_1 == 'C':
    nota_1 = 2
elif materia_1 == 'E':
    nota_1 = 0

if materia_2 == 'A':
    nota_2 = 4
elif materia_2 == 'B':
    nota_2 = 3
elif materia_2 == 'C':
    nota_2 = 2
elif materia_2 == 'E':
    nota_2 = 0

if materia_3 == 'A':
    nota_3 = 4
elif materia_3 == 'B':
    nota_3 = 3
elif materia_3 == 'C':
    nota_3 = 2
elif materia_3 == 'E':
    nota_3 = 0

if materia_4 == 'A':
    nota_4 = 4
elif materia_4 == 'B':
    nota_4 = 3
elif materia_4 == 'C':
    nota_4 = 2
elif materia_4 == 'E':
    nota_4 = 0

if (materia_1  == 'E' or materia_2  == 'E'  or materia_3  == 'E' or materia_4  == 'E'):
    resultado = 'false'
else:
    if (nota_1 + nota_2 + nota_3 + nota_4) / 4 >= 3:
        resultado = 'true'
    else:
        resultado = 'false'

print(resultado)