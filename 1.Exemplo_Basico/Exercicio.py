import unittest

def multipla(a, b):
    return a * b

class TestMultiplicacao(unittest.TestCase):

    def test_multiplicacao(self):
        self.assertEqual(multipla(3,3), 9)
        self.assertTrue(multipla(3,0) == 0)

if __name__ == "__main__":
    unittest.main()