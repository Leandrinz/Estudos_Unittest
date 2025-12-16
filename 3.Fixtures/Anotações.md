--- FIXTURES ---
1. O que são:
    . São métodos especiais usados para:
        . Preparar o ambiente do teste
        . Criar objetos
        . Abrir arquivos / conexões
        . Limpar tudo no final, garantindo isolamento e previsibilidade.

2. Ciclo de vida completo:
    . Ordem real da execução:
        setUpModule()    # 1 vez (Arquivo)
        setUpClass()     # 1 vez (classe)

        setUp()          # 1 vez (classe)
        test_x()       
        tearDown()       # depois de cada teste

        (repetido para cada test_)

        tearDownClass()  # 1 vez (classe)
        tearDownModule() # 1 vez (arquivo)

3. Fixtures de nível de método:
    setUp() / tearDown() - Executam antes de cada teste

    Exemplo:
        import unittest

        class TestExemplo(unittest.TestCase):

            def setUp(self):
                self.valor = 10
                #print("setUp")

            def tearDown(self):
                #print("tearDown")

            def test_a(self):
                self.assertEqual(self.valor, 10)

            def test_b(self):
                self.assertTrue(self.valor > 0)
    
    Saída no terminal:
        setUp
        tearDown
        setUp
        tearDown

4. Fixtures de nível de classe
    setUpClass() / tearDownClass() - Executam uma única vez para a classe inteira.

    . Devem ser métodos de classe:
        @classmethod
        def setUpClass(cls):
            . . .

    
        . Exemplo:
            class TestClasse(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                cls.base = 100
                print("setUpClass")

            @classmethod
            def tearDownClass(cls):
                print("tearDownClass")

            def test_um(self):
                self.assertEqual(self.base, 100)

            def test_dois(self):
                self.assertTrue(self.base > 0)
        
5. Fixtures de nível de módulo
    setUpModule() / tearDownModule() - Ficam fora das classes
    . Executam uma vez por arquivo

    Exemplo:
        def setUpModule():
            print("setUpModule")
        
        def tearDownModule():
            print("tearDownModule")
        
        

