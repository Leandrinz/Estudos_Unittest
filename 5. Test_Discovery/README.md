# 🧪 Test Discovery (unittest)

---

## 📌 1) O que é Test Discovery

Test Discovery é o mecanismo que:

* Procura automaticamente arquivos, classes e métodos de teste
* Executa todos os testes sem precisar chamar cada arquivo manualmente

### ▶️ Comando principal

```bash
python -m unittest discover
```

---

## 📁 2) Estrutura de pastas (padrão recomendado)

### Exemplo de projeto

```
projeto/
|
|-- calculadora.py
|
|__ tests/
    |-- test_media.py
    |-- test_soma.py
    |-- test_subtracao.py
```

### 📌 Regras importantes

* Arquivos devem começar com `test_`
* Pasta de testes geralmente chamada `tests` (não obrigatório)
* Classes devem herdar de `TestCase`
* Métodos devem começar com `test_`

---

## 🔍 3) Como o discovery funciona

Ao rodar:

```bash
python -m unittest discover
```

O `unittest` executa:

1. Procura arquivos `test*.py`
2. Dentro deles, procura classes que herdam de `TestCase`
3. Dentro das classes, procura métodos `test_`
4. Executa tudo automaticamente

---

## ⚠️ 4) Quando NÃO usar unittest.main()

Com Test Discovery:

* `unittest.main()` não é necessário
* Pode existir no arquivo, mas será ignorado

Em projetos reais, normalmente não se usa:

```python
if __name__ == "__main__":
    unittest.main()
```

---

## 🚀 Comando completo (recomendado)

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 📌 Parâmetros

* `-s tests` → pasta onde estão os testes
* `-p "test_*.py"` → padrão dos arquivos
* `-v` → modo verboso (mais detalhes na saída)
