valor = 1
valor_final = 0

while valor != 0:
    valor = float(input("Digite um valor inteiro e positivo ou 0 para terminar: "))
    if valor > 0:
        valor_final = valor_final + valor
    elif valor < 0:
        print("Valor invalido")
        valor = 1

if valor_final > 1000:
    valor_final = valor_final * 0.9

print(f"O valor Total da compra foi de: R${float(valor_final)}")