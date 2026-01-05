def pegar_idade():
    return int(input("Idade: "))

def buscar_saldo():
    return int(input("Saldo: "))


def pode_pegar_emprestimo(valor):
    idade = pegar_idade()
    saldo = buscar_saldo()

    if idade < 0:
        raise ValueError("Idade inválida")
    
    if saldo < 0:
        raise ValueError("Saldo inválido")
    
    if idade < 21:
        return False
    
    return saldo >= valor