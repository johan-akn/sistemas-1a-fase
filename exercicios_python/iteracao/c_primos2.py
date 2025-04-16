x = int(input())
y = int(input())
num = max(x, y)
i = min(x, y)
cont = 0

if num <= 1:
    primo = False
else:
    while i*i <= num:
        if num % i != 0:
            cont += 1
        i += 1
        
print(cont)