inter = 0
finter = 0

for x in range(1,11):
    n = int(input("Digite um numero: "))
    
    if n >= 10 and n <= 20:
        inter = inter + 1
    else:
        finter = finter + 1

print("Quantidade de numeros DENTRO do intervalo: ", inter)
print("Quantidade de numeros FORA do intervalo: ", finter)