dias = int(input())
km_rodados = float(input())

custo_dia = 45.00
custo_km = 0.50

if km_rodados / dias > 60:
    valor_final = (dias * custo_dia) + ((km_rodados - (60 * dias)) * custo_km)
else: valor_final = dias * custo_dia

print(f'{valor_final:.2f}') 