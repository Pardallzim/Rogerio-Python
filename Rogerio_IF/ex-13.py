x = 1
s = 0
m = 0
ix = 0
while x != 0:
    x = int(input("Digite um numero: "))
    if x != 0:
        s = s + x
        ix = ix + 1 
    else:
        m = s / ix
        print("A soma dos números é: ", s, "e a Media é: ",m)