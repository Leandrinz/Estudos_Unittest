# 🧪 TestCase (unittest)

Este guia explica de forma clara e organizada como funciona o **TestCase** no módulo `unittest` do Python.

---

# 📌 1. O que é um TestCase?

Um **TestCase** é uma unidade de teste, como uma “caixa” que contém:

* Métodos de teste (`test_...`)
* Métodos auxiliares (`setUp`, `tearDown`)
* Asserções (`assertEqual`, `assertTrue`, etc.)

Cada TestCase representa um conjunto de testes sobre algo específico.

### 🔎 Exemplo

```python
import unittest

class TestMath(unittest.TestCase):
    pass
```

---

# 🔍 2. Como o unittest descobre testes?

O `unittest` segue duas regras principais:

### ✅ Regra 1: Herança obrigatória

A classe deve herdar de `unittest.TestCase`:

```python
class TesteA(unittest.TestCase):  # ✔️ executado
    pass

class MinhaClasse:  # ❌ ignorado
    pass
```

---

### ✅ Regra 2: Nome dos métodos

Somente métodos que começam com `test_` são executados:

```python
def test_soma(self):  # ✔️ executado
    pass

def soma(self):  # ❌ ignorado
    pass
```

---

# 🔄 3. Cada teste roda isolado

Cada método de teste é executado em uma **nova instância** da classe.

Isso significa:

* `setUp()` roda antes de cada teste
* `tearDown()` roda depois de cada teste
* Um teste NÃO interfere no outro

### 🔎 Exemplo

```python
class Teste(unittest.TestCase):

    def test_a(self):
        pass

    def test_b(self):
        pass
```

### 🧠 Execução:

```
setUp -> test_a -> tearDown
setUp -> test_b -> tearDown
```

✔️ Cada teste é totalmente isolado.

---

# 🧠 4. Por que usar "self"?

O `self` é necessário porque:

* Cada teste é um método da classe
* Os asserts pertencem à instância (`self.assertEqual`, etc.)

### 📌 O `self` permite:

* Chamar métodos de asserção
* Armazenar dados no `setUp`
* Compartilhar dados dentro do mesmo teste

⚠️ Importante: dados NÃO são compartilhados entre testes diferentes.

---

# 🧩 5. Organização de testes

Você pode organizar seus testes de duas formas:

* Vários métodos `test_` dentro de uma mesma classe
* Múltiplas classes de teste

### 🔎 Exemplo

```python
class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(2 + 3, 5)

    def test_soma_negativos(self):
        self.assertEqual(-2 + -1, -3)


class TestMultiplicacao(unittest.TestCase):

    def test_multiplicacao(self):
        self.assertEqual(3 * 4, 12)
```

### 🧠 Ordem de execução:

1. TestSoma.test_soma_positivos
2. TestSoma.test_soma_negativos
3. TestMultiplicacao.test_multiplicacao

---

# 🚀 Resumo Rápido

* TestCase = conjunto de testes
* Deve herdar de `unittest.TestCase`
* Métodos devem começar com `test_`
* Cada teste roda isoladamente
* `self` é obrigatório
* Pode organizar em classes e métodos

---
