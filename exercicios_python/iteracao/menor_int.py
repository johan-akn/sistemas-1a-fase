x = 1
fatorial = 1
num_decima = 2

while fatorial <= num_decima:
    num_decima = x**10
    
    for i in range (x, 1, -1):
        fatorial *= i
    x += 1
    
print(x)