--- EXEMPLO BÁSICO -> UNITTEST ---

1) Toda classe de teste herda de unittest.TestCase
    ex:
        import unittest

        class TesteExemplo(unittest.TestCase):
            pass

2) Todo método que começa com test_ é reconhecido automaticamente (igual no pytest)
    ex: 
        def test_soma(self):
            self.assertEqual(1 + 2, 3)

3) unittest.main() vai rodar os testes
    ex:
        if __name__ == "__main__":
            unittest.main()