# 🧪 side_effect (unittest)

---

## 📌 O que é

Enquanto `return_value` define um valor fixo de retorno:

```python
mock.return_value = 10
```

`side_effect` permite definir um comportamento ao chamar a função.

---

## 🧠 O que o side_effect pode fazer

* Lançar uma exceção
* Retornar valores diferentes a cada chamada
* Simular erros reais (input inválido, falhas externas, etc.)

---

## 🔧 Exemplos

### 🔁 Retorno fixo

```python
mock.return_value = 10
```

Sempre retorna `10`.

---

### 🔄 Retornos diferentes por chamada

```python
mock.side_effect = [10, 20, 30]
```

* 1ª chamada → 10
* 2ª chamada → 20
* 3ª chamada → 30

---

### ⚠️ Simular erro

```python
mock.side_effect = ValueError("erro")
```

Ao chamar a função, uma exceção será lançada.

---

## 🚀 Resumo

* `return_value` → retorno fixo
* `side_effect` → comportamento dinâmico
* Ideal para simular cenários reais e erros
