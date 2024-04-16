import unittest
from calculadora import Funcoes_aleatorios
a = None
b = 1
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]

class Teste_instancia():
    def __init__(self) -> None:
        pass

x = Teste_instancia()

class Teste_funcoes_aleatorios(unittest.TestCase):
    def setUp(self) -> None:
        self.func = Funcoes_aleatorios()

    def test_soma(self):
        self.assertEqual(self.func.soma(10,10),20)
        self.assertNotEqual(self.func.soma(10,10),21)

    def test_true(self):
        self.assertTrue(self.func.true())

    def test_false(self):
        self.assertFalse(self.func.false())

    def test_is_not(self):
        self.assertIs(1,1)

    def test_is_not(self):
        self.assertIsNot(1,2)

    def test_is_none(self):
        self.assertIsNone(a)
        
    def test_not_none(self):
        self.assertIsNotNone(b)

    def test_list(self):
        self.assertListEqual(lista1, lista2)

    def test_instancia(self):
        self.assertIsInstance(x,Teste_instancia)

    def test_in(self):
        self.assertIn(5,lista1)
    
    def test_not_in(self):
        self.assertNotIn(6,lista1)

    def test_sequencia(self):
        self.assertSequenceEqual("1","1")

if __name__ == '__main__':
    unittest.main()

