class Quadrado:
    def __init__(self, tamanho_lado:float):
        self.tamanho_lado = tamanho_lado

    def mudar_lado(self, novo_valor):
        self.tamanho_lado = novo_valor

    def mostrar_lados(self):
        return f"Os lados do quadrado tem: {self.tamanho_lado}"

    def calcular_area(self):
        area = self.tamanho_lado * self.tamanho_lado
        return f"o tamanho do lado é: {self.tamanho_lado} e a area é de: {area}"

tamanho_lado =float(input("Digite o tamanho do lado: "))

quadrado = Quadrado(tamanho_lado)
print(quadrado.mostrar_lados())
print(quadrado.calcular_area())
novo_valor =float(input("Digite o novo tamanho do lado: "))
quadrado.mudar_lado(novo_valor)
print(quadrado.mostrar_lados())
print(quadrado.calcular_area())