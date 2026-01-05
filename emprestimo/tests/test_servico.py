import unittest
from unittest.mock import patch
from servico import buscar_saldo
from servico import pegar_idade
from servico import pode_pegar_emprestimo

class Test_Emprestimo(unittest.TestCase):
    # Tudo certo
    @patch("servico.pegar_idade")
    @patch("servico.buscar_saldo")
    def test_pode_pegar_emprestimo_com_sucesso(self, mock_saldo, mock_idade):
        mock_idade.return_value = 25
        mock_saldo.return_value = 100

        self.assertTrue(pode_pegar_emprestimo(50))
    
    # Idade insuficiente
    @patch("servico.pegar_idade")
    @patch("servico.buscar_saldo")
    def test_idade_menor_que_21(self, mock_saldo, mock_idade):
        mock_idade.return_value = 18
        mock_saldo.return_value = 1000

        self.assertFalse(pode_pegar_emprestimo(50))
    
    # Saldo insuficiente
    @patch("servico.pegar_idade")
    @patch("servico.buscar_saldo")
    def test_saldo_insuficiente(self, mock_saldo, mock_idade):
        mock_idade.return_value = 22
        mock_saldo.return_value = 10

        self.assertFalse(pode_pegar_emprestimo(50))

    # Idade inválida
    @patch("servico.pegar_idade")
    @patch("servico.buscar_saldo")
    def test_idade_invalida(self, mock_saldo, mock_idade):
        mock_idade.return_value = -1
        mock_saldo.return_value = 100

        with self.assertRaises(ValueError):
            pode_pegar_emprestimo(50)
    
    # Saldo inválido
    @patch("servico.pegar_idade")
    @patch("servico.buscar_saldo")
    def test_saldo_invalido(self, mock_saldo, mock_idade):
        mock_idade.return_value = 25
        mock_saldo.return_value = -1

        with self.assertRaises(ValueError):
            pode_pegar_emprestimo(50)