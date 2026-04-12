# 🧪 Fixtures (unittest)

# 📌 1. O que são

Fixtures são métodos especiais usados para:

* Preparar o ambiente do teste
* Criar objetos
* Abrir arquivos ou conexões
* Limpar tudo no final

Garantem isolamento e previsibilidade nos testes.

---

# 🔄 2. Ciclo de vida completo

Ordem real de execução:

```
setUpModule()    # 1 vez (arquivo)
setUpClass()     # 1 vez (classe)

setUp()          # antes de cada teste
test_x()
tearDown()       # depois de cada teste

(repetido para cada test_)

tearDownClass()  # 1 vez (classe)
tearDownModule() # 1 vez (arquivo)
```

---

# 🔧 3. Fixtures de nível de método

Executam antes e depois de cada teste:

* setUp()
* tearDown()

### Exemplo

```python
import unittest

class TestExemplo(unittest.TestCase):

    def setUp(self):
        self.valor = 10
        # print("setUp")

    def tearDown(self):
        # print("tearDown")
        pass

    def test_a(self):
        self.assertEqual(self.valor, 10)

    def test_b(self):
        self.assertTrue(self.valor > 0)
```

### Saída esperada

```
setUp
tearDown
setUp
tearDown
```

---

# 🧩 4. Fixtures de nível de classe

Executam uma única vez para toda a classe:

* setUpClass()
* tearDownClass()

Devem ser métodos de classe:

```python
import unittest

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
```

---

# 🧱 5. Fixtures de nível de módulo

Ficam fora das classes e executam uma vez por arquivo:

* setUpModule()
* tearDownModule()

### Exemplo

```python
def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")
```

---

# 🚀 Resumo

* Método: setUp / tearDown → antes/depois de cada teste
* Classe: setUpClass / tearDownClass → 1 vez por classe
* Módulo: setUpModule / tearDownModule → 1 vez por arquivo
