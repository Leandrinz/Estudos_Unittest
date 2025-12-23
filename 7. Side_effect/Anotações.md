--- SIDE_EFFECT ---
. O que é:
    Enquanto o return_value faz:
        "Quando a função for chamada, retorne X"
    O side_effect faz:
        "Quando a função for chamada, execute um comportamento"
        Esse comportamento pode ser:
            . Lançar uma execução
            . Retornar valores diferentes a cada chamada
            . Simular erro real (input inválido, falha externa, etc.)
    Exemplo:
        - mock.return_value = 10
            . Sempre retorna 10
        - mock.side_effect = [10, 20, 30]
            . 1ª Chamada -> 10
            . 2ª Chamada -> 20
            . 3ª Chamada -> 30
        - mock.side_effect = ValueError("erro")
            . Levanta exceção