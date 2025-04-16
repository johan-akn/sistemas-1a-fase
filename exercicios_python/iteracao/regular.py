def verificarNum(num):
    num = abs(num)
    
    if num == 0 or num == 1:
        return False
    
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
            
    return num == 1

num = int(input())

print(verificarNum(num))
