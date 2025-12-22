--- MOCK E PATCH ---

Ele resolve um problema clássico:
    "Como testar uma função que depende de uma outra coisa externa?"
    Exemplos de dependência:
        . Outra função
        . Acesso a arquivo
        . Input do usuário
        . API
        . Banco de dados

Problema real (sem mock):
    Temos como exemplo:
        # calculadora.py
        def buscar_numero():
            return int(input("Digite um número: "))

        def dobro():
            return buscar_numero() * 2
    Isso é péssimo para teste:
        . Exige input
        . Não é automático
        . Trava o teste

Solução: MOCK
    Com mock, você finge o comportamento de função externa
    
    Conceito chave:
        Mock = substituir temporariamente uma dependência por um valor controlado
    
    Exemplo básico com patch:

        import unittest
        from unittest.mock import patch
        from calculadora import dobro

        class TestDobro(unittest.TestCase):

            @patch("calculadora.buscar_numero")
            def test_dobro(self, mock_buscar):
                mock_buscar.return_value = 5
                self.assertEqual(dobro(), 10)
    
    O que aconteceu:
        @patch("calculadora.buscar_numero") → substitui a função real

        mock_buscar.return_value = 5 → força o retorno

        dobro() usa o valor falso sem saber


