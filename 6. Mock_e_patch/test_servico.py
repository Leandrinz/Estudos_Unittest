import unittest
from unittest.mock import patch
from servico import pode_dirigir
from servico import pode_comprar

class TestPodeDirigir(unittest.TestCase):

    @patch("servico.pegar_idade")
    def test_pode_dirigir_maior_de_idade(self, mock_idade):
        mock_idade.return_value = 20
        self.assertTrue(pode_dirigir())
    
    @patch("servico.pegar_idade") # O patch aponta PARA ONDE A FUNÇÃO É USADA
    def test_pode_dirigir_menor_de_idade(self, mock_idade):
        mock_idade.return_value = 16
        self.assertFalse(pode_dirigir())
    
    @patch("servico.buscar_saldo")
    def test_saldo_maior_que_valor(self, mock_saldo):
        mock_saldo.return_value = 15
        self.assertTrue(pode_comprar(10))
    
    @patch("servico.buscar_saldo")
    def test_saldo_menor_que_valor(self, mock_saldo):
        mock_saldo.return_value = 10
        self.assertFalse(pode_comprar(15))
    
# No patch é sempre: arquivo.funcao
# O que o mock faz no mock_idade.return_value = 20: Isso significa "Quando pegar_idade() for chamada, retorne 20". A função real não roda
