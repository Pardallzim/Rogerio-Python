def contstring(string, letra):
    cont = 0
    for x in string:
        if x == letra:
            cont += 1
    
    return(cont)

a = str(input("Digite uma palavra: "))
b = str(input("Digite uma letra: "))

print(f"Quantidade de vezes que a letra {b} apareceu na string {a}:", contstring(a, b))