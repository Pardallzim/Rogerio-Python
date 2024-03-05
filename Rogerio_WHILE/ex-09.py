valor = 1
contador = 0
media = 0
soma = 0

while valor != 0:
    valor = float(input("Digite um valor inteiro ou 0 para terminar: "))
    if valor != 0:
        soma = soma + valor
        contador += 1

if contador > 0:
    media = soma / contador
else:
    print("Erro divisão por 0")

print(f"A soma é {soma} e a media {media}")