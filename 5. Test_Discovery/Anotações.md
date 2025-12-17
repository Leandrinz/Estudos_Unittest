--- TEST DISCOVERY ---

1) O que é Test Discovery:
    Test Discovery é o mecanismo que:
        Procura automaticamente arquivos, classes e métodos de teste e executa tudo sem precisar chamar cada arquivo.
    
    Comando principal:
        python -m unittest discover

2) Estrutura de pastas (padrão recomendado):
    Exemplo de projeto simples:

        projeto/
        |
        |-- calculadora.py
        |
        |__tests/
           |--test_media.py
           |--test_soma.py
           |--test_subtracao.py
    
    |Regras importantes:
        . Arquivo começar com test_
        . Pasta de testes se chamar tests(não é obrigatório, mas fica organizado)
        . Classe herda TestCase
        . Métodos começam com test_

3) Como o discovery funciona (passo a passo):
    . Quando roda:
        python -m unittest discover

        O unittest:
            1. Procura arquivos test*.py
            2. Dentro deles, procura classes TestCase
            3. Dentro das classes, métodos test_
            4. Executa tudo automaticamente

4) Quando NÃO usar unittest.main():
    Com Test Discovery:
        . unittest.main() não é necessário
        . Ele pode até existir, mas é ignorado

    Em projetos reais, os arquivos de teste não precisam ter if __name__ == "__main__".

Rodar tudo: python -m unittest discover -s tests -p "test_*.py" -v
