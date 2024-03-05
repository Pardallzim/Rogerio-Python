numero = 1
maior = 0

while numero != 0:
    numero = int(input("Digite um numero inteiro e positivo ou 0 para terminar: "))
    if numero > maior:
        maior = numero

print(f"O maior numero digitado foi: {maior}")