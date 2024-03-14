def soma(valor1, valor2):
    x = valor1 + valor2
    return(x)

def sub(valor1, valor2):
    if valor1 > valor2:
        x = valor1 - valor2
    else:
        x = valor2 - valor1
    
    return(x)
    
def mult(valor1, valor2):
    x = valor1 * valor2
    return(x)

def div(valor1, valor2):
    x = valor1 / valor2
    return(x)

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print("Soma", soma(a, b))
print("Subtração", sub(a, b))
print("Multiplicação", mult(a, b))
print("Divisão", div(a, b))
