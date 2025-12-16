--- TESTCASE ---
# 1: O que é um TestCase?
    . É uma unidade de teste, uma "caixa" que irá conter:
        . métodos de teste (test_....)
        . métodos auxiliares (setUp, tearDown)
        . suas asserções (assertEqual, assertTrue...)
    Cada TestCase é como um conjunto de testes sobre algo específico.
    . Exemplo:
        class TestMath(unittest.TestCase):
            ..

# 2: Como o unittest descobre testes?
    . Ele segue duas regras:
        . Regra 1 --- Só classes que herdam de TestCase são testadas 
            ex:
                class TesteA(unittest.TestCase): # ok
                
                class MinhaClasse: # ignorado
        
        . Regra 2 --- só métodos começando com test_ são executados
            ex:
                test_soma(self): # executado

                def soma(self): # ignorado

# 3: Cada método de teste é executado em uma instância nova
    Isso significa que:
        . setUp() roda antes de cada teste
        . tearDown() roda depois de cada teste
        . Um teste não "vaza" valores para outro
    
    Exemplo:
        class Teste(unittest.TestCase):
            def test_a(self):
                pass
            
            def test_b(self):
                pass
    
    Aqui:
        setUp -> test_a -> tearDown
        setUp -> test_b -> tearDown

    Com isso, é evidente que cada teste é isolado.

# 4: Por que é necessário o self:
    Por que:
        . Cada teste é um método da classe
        . Você precisa acessar métodos da instância do TestCase
        . Os asserts são métodos da instância (self.assertEqual etc.)

    Então self é obrigatório para:
        . Chamar asserts
        . Armazenar valores criados no setUp
        . Compartilhar dados entre métodos do mesmo teste (mas nunca entre testes diferentes)

# 5: Como organizar vários testes:
    . É possível criar vários métodos test_ na mesma classe ou várias classes de teste
    Exemplo:
        class TestSoma(unittest.TestCase):
            def test_soma_positivos(self):
                self.assertEqual(2+3, 5)

            def test_soma_negativos(self):
                self.assertEqual(-2 + -1, -3)

        class TestMultiplicacao(unittest.TestCase):
            def test_multiplicacao(self):
                self.assertEqual(3*4, 12)

    O unittest executará:
        1. TestSoma.test_soma_positivos
        2. TestSoma.test_soma_negativos
        3. TestMultiplicacao.test_multiplicacao

