import unittest

def setUpModule():
    print(">> setUpModule")

def tearDownModule():
    print(">> tearDownModule")


class TesteCalculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = 10
        print(">> setUpClass")

    @classmethod
    def tearDownClass(cls):
        print(">> tearDownClass")

    
    def setUp(self):
        self.valor = 5
        print("setUp")
    
    def tearDown(self):
        print("tearDown")
    
    def test_soma_base_com_valor(self):
        resultado = self.base + self.valor
        self.assertEqual(resultado, 15)
    
    def test_valor_menor_que_base(self):
        self.assertTrue(self.valor < self.base)

    
