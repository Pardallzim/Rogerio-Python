def funcao(n):
    a = 2
    m = 3
    x = 0
    while a <= n:
        x = x + (a / m)
        a += 1
        m += 2
    else:
        print(x)

contador = True
while contador:
    n = int(input("digite um numero inteiro: "))
    if n > 0:
        contador = False
    else:
        continue

funcao(n)