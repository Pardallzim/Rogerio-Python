i = int(input("Digite um número inteiro e positivo: "))
a = int(input("Digite um valor pra A: "))
b = int(input("Digite um valor pra B: "))
c = int(input("Digite um valor pra C: "))

if (i % 2) == 0:
    print((a + b + c) / 3)
elif i > 10:
    print(((a * 2) + (b * 3) + (c *4)) / 9)