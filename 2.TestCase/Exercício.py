import unittest

def subtrai(a, b):
    return a - b


class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtrai(3,3), 0)
        self.assertTrue(subtrai(3, 3) == 0)
    
    def test_subtracao_negativos(self):
        self.assertEqual(subtrai(-3, -3), 0)
        self.assertTrue(subtrai(-3,-3) == 0)
    
    def test_subtracao_zero(self):
        self.assertTrue(subtrai(0, 0) == 0)
        self.assertEqual(subtrai(0,0), 0)

if __name__ == "__main__":
    unittest.main()