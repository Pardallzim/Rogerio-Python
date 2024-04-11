import unittest


class Calculadora:
    def __init__(self):
        pass

    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y
    


class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()

    def teste_soma(self):
        self.assertEqual(self.calc.soma(1,3), 4)
        self.assertEqual(self.calc.soma(300,400), 700)

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(5,4), 1)
        self.assertNotEqual(self.calc.subtracao(5,2), 4)


if __name__ == '__main__':
    unittest.main()