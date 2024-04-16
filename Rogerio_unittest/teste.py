import unittest

class Calculadora:
    def __init__(self) -> None:
        pass

    def soma(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def true(self):
        return True
    
    def false(self):
        return False

class TesteCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()

    def teste_soma(self):
        self.assertEqual(self.calc.soma(1,3), 4)

    def teste_sub(self):
        self.assertNotEqual(self.calc.sub(5, 6), 2)
        self.assertEqual(self.calc.sub(5, 6), -1)
        self.assertEqual(self.calc.sub(10, 6), 4)

    def teste_true(self):
        self.assertTrue(self.calc.true())

    def teste_false(self):
        self.assertFalse(self.calc.false())

if __name__ == '__main__':
    unittest.main()