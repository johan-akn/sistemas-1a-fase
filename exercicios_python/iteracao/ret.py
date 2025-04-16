while True:
    n = int(input())
    if n == 0:
        break
    total_pares = 0
    for _ in range(n):
        c, v = [int(w) for w in input().split()]
        total_pares += v // 2
        retangulos = total_pares // 2
    print(retangulos)
