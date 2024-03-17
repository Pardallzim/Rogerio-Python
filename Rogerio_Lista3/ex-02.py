def verifpar(valor1):
    if (valor1 % 2) == 0:
        return True
    else:
        return False

par = int(input("Digite um valor para verificar o par: "))

print("O número é par?", verifpar(par))