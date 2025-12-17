import unittest
from calculadora import media  # função que você quer testar

class TestMedia(unittest.TestCase):

    def test_resultado_correto(self):
        self.assertEqual(media(10, 0), 5)

    def test_valores_nao_numericos(self):
        with self.assertRaises(TypeError):
            media(10, "abc")

    def test_media_maior_que_zero(self):
        self.assertTrue(media(3, 2) > 0)

    def test_media_in_lista(self):
        self.assertIn(media(4, 6), [4, 5, 6])