class Bola:
    def __init__(self, cor:str, circunferencia:float, material:str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self):
        self.cor =str(input("Digite a nova cor: "))

    def mostrar_cor(self):
        print(f"A cor da bola é: {self.cor}")

    def __str__(self):
        return f"A cor da bola é: {self.cor} a circunferência é de: {self.circunferencia} e o material é: {self.material}"

cor =str(input("Digite a cor da bola: "))
circunferencia =float(input("Digite a circunferência da bola(em cm): "))
material =str(input("Digite o material da bola: "))

bola = Bola(cor, circunferencia, material)
print(bola)
bola.trocar_cor()
bola.mostrar_cor()