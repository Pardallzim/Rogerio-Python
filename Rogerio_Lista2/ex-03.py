contador = 0
vetor = []

def funcao(a):
    if a < 10 and a > 0:
        x = 1
        print(x)
    elif a < 0: 
        x = 0
        print(x)
    else:
        x = 2
        print(x)

contador = 0
while contador < 20:
    x = int(input("digite um numero positivo ou negativo para vetor: "))
    vetor.append(x)
    contador += 1

contador = 0
while contador < 20:
    x = vetor[contador]
    funcao(x)
    contador += 1