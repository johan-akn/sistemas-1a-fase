num = int(input())

fx = 1
fy = 0

if num > 1:
    for i in range (num - 1):
        fn = fx + fy
        fy = fx
        fx = fn
else:
    fn = 1
    
print(fn)

