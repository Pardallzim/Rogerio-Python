a = int(input("Digite a altura (em cm): "))
l = int(input("Digite a largura (em cm): "))
c = int(input("Digite a comprimento (em cm): "))

cd = int(input("Digite o consumo de água (em L/dias): "))

x = (a * l * c) / 1000
y = x // cd

print("capacidade em m³ é de: ", (a * l * c)//1000000)

print("A capacidade total do reservatorio é de: ", x,"Litros")
print("A autonomia do reservatorio é de: ", y,"Dias")

if y < 2:
    print("Consumo elevado")
elif y >= 2 and y < 7:
    print("Consumo moderado")
else:
    print("Consumo reduzido")