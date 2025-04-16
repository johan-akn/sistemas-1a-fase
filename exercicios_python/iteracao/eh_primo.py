num = int(input())

if num <= 1:
    primo = False
else:
    i = 2
    while i*i <= num:
        if num % i == 0:
            primo = False
            break
        i += 1
        
print(primo)