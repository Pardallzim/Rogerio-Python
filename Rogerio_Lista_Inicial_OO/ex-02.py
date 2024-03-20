class Quadrado:
    def __init__(self, tamanho_lado:float):
        self.tamanho_lado = tamanho_lado

    def mudar_lado(self):
        self.tamanho_lado =float(input("Digite o novo tamanho do lado: "))

    def __str__(self):
        return f"o tamanho do lado é: {self.tamanho_lado} e a area é de: {self.tamanho_lado * self.tamanho_lado}"

tamanho_lado =float(input("Digite o tamanho do lado: "))

quadrado = Quadrado(tamanho_lado)

print(quadrado)
quadrado.mudar_lado()
print(quadrado)
    