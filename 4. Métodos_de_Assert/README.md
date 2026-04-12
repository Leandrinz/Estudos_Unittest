# 🧪 Métodos de Assert (unittest)

---

## 📌 1) assertEqual(a, b)

Verifica se dois valores são iguais.

```python
self.assertEqual(2 + 2, 4)
```

Usar para:

* Números
* Strings
* Listas
* Dicionários
* Retorno de funções

---

## 📌 2) assertNotEqual(a, b)

Contrário do `assertEqual`.

```python
self.assertNotEqual(2 + 2, 5)
```

---

## 📌 3) assertTrue(expr) / assertFalse(expr)

Verifica se uma expressão é verdadeira ou falsa.

```python
self.assertTrue(10 > 5)
self.assertFalse(3 > 10)
```

Usar quando:

* A condição é lógica
* Não faz sentido usar `assertEqual`

---

## 📌 4) assertIn(item, container)

Verifica se um elemento está contido em outro.

```python
self.assertIn(3, [1, 2, 3])
self.assertIn("a", "banana")
```

---

## 📌 5) assertNotIn(item, container)

Contrário do `assertIn`.

```python
self.assertNotIn(4, [1, 2, 3])
```

---

## 📌 6) assertIs(a, b) / assertIsNot(a, b)

Verifica identidade (mesmo objeto em memória).

```python
self.assertIs(a, b)
self.assertIsNot(a, b)
```

Usar com:

* `None`
* Objetos
* Singletons

```python
self.assertIs(valor, None)
```

---

## 📌 7) assertIsNone() / assertIsNotNone()

Atalhos para verificação com `None`.

```python
self.assertIsNone(resultado)
self.assertIsNotNone(resultado)
```

---

## 📌 8) assertRaises()

Testa se uma exceção é lançada.

Forma recomendada com `with`:

```python
with self.assertRaises(ValueError):
    int("abc")
```

Usar quando:

* A função deve falhar
* Validação de erro
