senha = str(input("Digite a sua senha: "))
confirmacao_senha = "!"

while senha != confirmacao_senha:
    confirmacao_senha = str(input("Confirme sua senha: "))
else:
    print("Senha Correta")