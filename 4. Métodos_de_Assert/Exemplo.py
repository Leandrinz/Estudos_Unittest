import unittest

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b

class TestDivisao(unittest.TestCase):

    def test_divisao_ok(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_resultado_tipo(self):
        resultado = dividir(10, 2)
        self.assertIsNotNone(resultado)
