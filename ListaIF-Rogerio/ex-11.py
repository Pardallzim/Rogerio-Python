a = int(input("Digite um valor pra A: "))
b = int(input("Digite um valor pra B: "))
c = int(input("Digite um valor pra C: "))

if (a > b and a < c) or (a > c and a < b ):
    print("A mediana é a letra A")
elif (b > a and b < c) or (b > c and b < a ):
    print("A mediana é a letra B")
elif (c > b and c < a) or (c > a and c < b ):
    print("A mediana é a letra C") 