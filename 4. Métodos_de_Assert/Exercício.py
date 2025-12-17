import unittest

def media(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Erro! Valor diferente de número identificado")
    return (a + b) / 2

class TestMedia(unittest.TestCase):
    
    def test_resultado_correto(self):
        self.assertEqual(media(9,1), 5)

    def test_verifica_veracidade(self):
        self.assertTrue(media(1, 2) > 1)
    
    def test_In(self):
        self.assertIn(media(10, 10), [1, 10, 20])

    def test_valores_nao_inteiros(self):
        with self.assertRaises(TypeError):
            media(10, "Vasco")
