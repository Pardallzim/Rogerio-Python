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
    
y = None


class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()

    def teste_soma(self):
        self.assertEqual(self.calc.soma(1,3), 4)
        self.assertEqual(self.calc.soma(300,400), 700)

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(5,4), 1)
        self.assertNotEqual(self.calc.subtracao(5,2), 4)

    def teste_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(4,5), 20)
        self.assertNotEqual(self.calc.multiplicacao(4,5), 21)

    def teste_divisao(self):
        self.assertEqual(self.calc.divisao(20,5), 4)
        self.assertNotEqual(self.calc.divisao(20,5), 3)
        self.assertNotEqual(self.calc.divisao(20,0), 3)

    def teste_is(self):
        self.assertIs(12,12)
        self.assertIsNot(10,12)
    
    def teste_none(self):
        self.assertIsNone(y)
        


if __name__ == '__main__':
    unittest.main()