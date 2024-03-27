class Retangulo:
    def __init__(self, comprimento:float, largura:float):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lado(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def mostrar_lados(self):
        return f"O comprimento é: {self.comprimento} e a largura é: {self.largura}"

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return self.comprimento + self.comprimento + self.largura + self.largura

    def __str__(self):
        return f"o tamanho do comprimento é: {self.comprimento} e a altura é de: {self.largura} sua area é de: {self.area} e seu perimetro é de: {self.perimetro}"

comprimento =float(input("Digite o tamanho do comprimento do piso: "))
largura =float(input("Digite o tamanho do largura do piso: "))

retangulo = Retangulo(comprimento, largura)

local_comprimento =float(input("Digite o tamanho do comprimento do local: "))
local_largura =float(input("Digite o tamanho do largura do local: "))

local = Retangulo(local_comprimento, local_largura)

quantpisos = local.calcular_area() / retangulo.calcular_area()
quantrodapes = local.calcular_perimetro() / largura

print(f"Quantidade de pisos nescesarios: {quantpisos} e quantidade de rodapés nescesarios: {quantrodapes}")