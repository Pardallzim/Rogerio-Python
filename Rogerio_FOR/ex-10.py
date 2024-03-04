x = int(input("Digite um número inteiro: "))

for y in range(x, 1, -1):
    x = x * (y - 1)

if x == 0:
    x = 1

print(x)
