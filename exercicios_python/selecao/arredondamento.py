nota = float(input())
nota_int = int(nota)
decimal = nota - nota_int

if decimal < 0.25:
    nota_final = float(nota_int)
elif 0.25 <= decimal < 0.75:
    nota_final = float(nota_int + 0.5)
else:
    nota_final = float(nota_int + 1.0)

print(nota_final)