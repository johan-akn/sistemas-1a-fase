decimal = int(input())
bin = ''

if decimal == 0:
    bin.append(0)
    
while decimal > 0:
    bin = str(decimal%2) + bin
        
print(bin)