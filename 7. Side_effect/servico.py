def pegar_idade():
    return int(input("Digite sua idade: "))

def pode_dirigir():
    idade = pegar_idade()
    if idade < 0:
        raise ValueError("Idade inválida")
    return idade >= 18

def buscar_saldo():
    return int(input("Digite o saldo: "))

def pode_comprar(valor):
    saldo = buscar_saldo()
    if saldo < valor:
        raise ValueError("Saldo insuficiente")
    return True