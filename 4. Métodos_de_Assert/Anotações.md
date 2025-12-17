--- MÉTODOS DE ASSERT DO TESTCASE ---

1) assertEqual(a, b):
    Verifica se dois valores são iguais.
    
    self.assertEqual(2 + 2, 4)

    Usar para:
        . Números
        . Strings
        . Listas
        . Dicionários
        . Retorno de funções

2) assertNotEqual(a, b):
    Contrário do assertEqual

3) assertTrue(expr) / assertFalse(expr):
    Verifica se uma expressão é verdadeira ou falsa.

    self.assertTrue(10 > 5)
    self.assertFalse(3 > 10)

    Usar quando:
        . A condição é lógica
        . Não faz sentido usar o assertEqual

4) assertIn(item, container):
    Verifica se algo está dentro de algo.

    self.assertIn(3, [1, 2, 3])
    self.assertIn("a", "banana")

5) assertNotIn(item, container):
    Contrário do assertIn

6) assertIs(a, b) / assertIsNot(a, b):
    self.assertIs(a, b) # mesmo objeto
    self.assertIsNot(a, b)

    Usar com:
        . None
        . objetos
        . singletons 

        self.assertIs(valor, None)
    
7) assertIsNone() / assertIsNotNone():
    self.assertIsNone(resultado)
    self.assertIsNotNone(resultado)

8) assertRaises():
    Testa exceções.

    Forma com with(recomendado):
        with self.assertRaises(ValueError):
            int ("abc")

    Usar quando:
        . A função deve falhar
        . Validação de erro