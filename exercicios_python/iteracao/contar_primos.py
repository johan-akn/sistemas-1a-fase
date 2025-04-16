x = int(input())
y = int(input())

maior = max(x, y)
i = min(x, y)
cont = 0

while i <= maior:
    if i % 2 != 0 and i % 3 != 0:  
        cont += 1
    if i == 2 or i == 3:
        cont += 1
    if i == 1:
        cont = 0
    i += 1
    
print(cont)