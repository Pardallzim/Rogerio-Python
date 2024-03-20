import math

class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, number1, number2):
        print("Soma:", number1 + number2)
    
    def subtrair(self, number1, number2):
        print("Subtração:", number1 - number2)
    
    def multiplicar(self, number1, number2):
        print("Multiplicação:", number1 * number2)
    
    def dividir(self, number1, number2):
        if number2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print("Divisão:", number1 / number2)
    
    def porcentagem(self, number1, number2):
        print("Porcentagem:", (number1 * number2) / 100)
    
    def raiz_quadrada(self, number1):
        print("Raiz quadrada:", math.sqrt(number1))
    
    def potenciacao(self, number1, number2):
        print("Potenciação:", number1 ** number2)

calc = Calculadora()

calc.somar(10, 2)
calc.subtrair(10, 8)
calc.multiplicar(4, 10)
calc.dividir(8, 0)
calc.dividir(65, 8)
calc.porcentagem(200, 40)
calc.raiz_quadrada(81)
calc.potenciacao(2, 5)
calc.somar(99, 1)