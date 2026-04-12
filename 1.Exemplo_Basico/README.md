# 🧪 Anotações: Exemplo Básico com unittest (Python)

O módulo `unittest` é uma biblioteca padrão do Python usada para criar e executar testes automatizados.

---

## 📌 Estrutura Básica

### 1️⃣ Classe de teste

Toda classe de teste deve herdar de `unittest.TestCase`:

```python
import unittest

class TesteExemplo(unittest.TestCase):
    pass
```

---

### 2️⃣ Métodos de teste

Todo método que começa com `test_` é automaticamente reconhecido como um teste:

```python
def test_soma(self):
    self.assertEqual(1 + 2, 3)
```

✔️ O método `assertEqual` verifica se os valores são iguais.

---

### 3️⃣ Executar os testes

O comando abaixo executa todos os testes definidos:

```python
if __name__ == "__main__":
    unittest.main()
```

---

# 🧠 Dicas Importantes

* Os testes devem ser **independentes entre si**.
* Use métodos como:

  * `assertEqual(a, b)` → verifica igualdade
  * `assertTrue(x)` → verifica se é verdadeiro
  * `assertFalse(x)` → verifica se é falso
* Nomeie bem os testes para facilitar a leitura.

---

# 🚀 Exemplo Completo

```python
import unittest

class TesteExemplo(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(1 + 2, 3)

    def test_multiplicacao(self):
        self.assertEqual(2 * 3, 6)

if __name__ == "__main__":
    unittest.main()
```

