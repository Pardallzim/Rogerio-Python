i = True
soma = 0

while i:
    numero = int(input("Digite um numero ou 0 para terminar: "))
    soma = soma + numero
    if i == 0:
        i = False

print(f"A soma dos numeros é {soma}")