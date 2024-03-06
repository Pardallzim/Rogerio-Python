senha = str(input("Digite sua senha: "))
i = True 

while i:
    while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")
    while len(senha) < 6 or len(senha) > 12:
        senha = input("A senha deve ter de 6 a 12 caracteres: ")
    while senha.isalpha():
        senha = input("Necessita de um numero: ")
    while senha.isalnum():
        senha = input("Necessita de um Caractere Especial: ")
    else:
        i = False