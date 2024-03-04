m = int(input("Digite um numero Minimo: "))
x = int(input("Digite um numero Maximo: "))
x = x + 1
par = 0
impar = 0 

for y in range(m, x):
    if (y % 2) == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Numeros pares: ", par)
print("Numeros Impares: ", impar)