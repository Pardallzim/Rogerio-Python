i = True
maior = 0

while i:
    numero = int(input("Digite um numero inteiro e positivo ou 0 para terminar: "))
    if numero > maior:
        maior = numero

    if numero == 0:
        i = False

print(f"O maior numero digitado foi: {maior}")