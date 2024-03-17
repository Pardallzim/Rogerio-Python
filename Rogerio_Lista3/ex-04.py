def IMC(peso, altura):
    x = peso / (altura * altura)

    return(x)

kg = float(input("Digite o peso(em kg): "))
tam = float(input("Digite a altura(em metros): "))

print(f"O IMC da pessoa que tem {kg} quilos e {tam} de altura sera de: ", IMC(kg,  tam) "kg/m2")