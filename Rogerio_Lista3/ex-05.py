import string
import secrets

def senha_aleatoria(tamanho):
    senha_argumentos = string.ascii_letters + string.digits + string.punctuation
    senha = " ".join(secrets.choice(senha_argumentos) for i in range(tamanho))
    return(senha)

tam = int(input("Digite o tamanho da sua senha: "))

print(f"A senha de tamanho {tam} é: ", senha_aleatoria(tam))
