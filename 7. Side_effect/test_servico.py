import unittest
from unittest.mock import patch
from servico import pode_dirigir
from servico import pode_comprar

class TestPodeDirigir(unittest.TestCase):

    @patch("servico.pegar_idade")
    def test_idade_invalida(self, mock_idade):
        mock_idade.side_effect = ValueError("Idade inválida")

        with self.assertRaises(ValueError):
            pode_dirigir()
    # Aqui estamos simulando

    # Testando múltiplas chamadas:
    @patch("servico.pegar_idade")
    def test_multiplas_idades(self, mock_idade):
        mock_idade.side_effect = [17, 18]

        self.assertFalse(pode_dirigir()) # 17
        self.assertTrue(pode_dirigir()) # 18
    

    @patch("servico.buscar_saldo")
    def test_saldo_invalido(self, mock_saldo):
        mock_saldo.side_effect = ValueError("Saldo inválido")

        with self.assertRaises(ValueError):
            pode_comprar(10)

    @patch("servico.buscar_saldo")
    def test_multiplos_saldos(self, mock_saldo):
        mock_saldo.side_effect = [5, 20]

        with self.assertRaises(ValueError):
            pode_comprar(10) # 5 < 10 -> Erro

        self.assertTrue(pode_comprar(10)) # 20
# No patch é sempre: arquivo.funcao