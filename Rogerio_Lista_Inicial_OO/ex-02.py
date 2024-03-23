class Quadrado:
    def __init__(self, tamanho_lado:float):
        self.tamanho_lado = tamanho_lado

    def mudar_lado(self):
        self.tamanho_lado =float(input("Digite o novo tamanho do lado: "))

    def mostrar_lados(self):
        print(f"Os lados do quadrado tem: {self.tamanho_lado}")

    def calcular_area(self):
        self.calcular_area = self.tamanho_lado * self.tamanho_lado
        return f"o tamanho do lado é: {self.tamanho_lado} e a area é de: {self.calcular_area}"

tamanho_lado =float(input("Digite o tamanho do lado: "))

quadrado = Quadrado(tamanho_lado)
quadrado.mudar_lado()
quadrado.mostrar_lados()
print(quadrado.calcular_area())