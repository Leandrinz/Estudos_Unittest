# 🧪 Mock e Patch (unittest)

---

## 📌 Problema que o Mock resolve

Como testar funções que dependem de algo externo?

### Exemplos de dependência:

* Outra função
* Acesso a arquivo
* Input do usuário
* API
* Banco de dados

---

## ⚠️ Problema real (sem mock)

```python
# calculadora.py

def buscar_numero():
    return int(input("Digite um número: "))


def dobro():
    return buscar_numero() * 2
```

Problemas:

* Exige input manual
* Não é automático
* Trava o teste

---

## 💡 Solução: Mock

Mock permite simular comportamentos externos.

### 🧠 Conceito-chave

Mock = substituir temporariamente uma dependência por um valor controlado

---

## 🔧 Exemplo com patch

```python
import unittest
from unittest.mock import patch
from calculadora import dobro

class TestDobro(unittest.TestCase):

    @patch("calculadora.buscar_numero")
    def test_dobro(self, mock_buscar):
        mock_buscar.return_value = 5
        self.assertEqual(dobro(), 10)
```

---

## 🔍 O que aconteceu

* `@patch("calculadora.buscar_numero")` → substitui a função real
* `mock_buscar.return_value = 5` → define o valor retornado
* `dobro()` usa o valor falso sem saber

---

## 🧠 Resumo

* Mock evita dependências externas em testes
* Torna testes automáticos e previsíveis
* Patch substitui funções temporariamente
