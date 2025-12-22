def pegar_idade():
    return int(input("Digite sua idade: "))

def pode_dirigir():
    idade = pegar_idade()
    return idade >= 18

def buscar_saldo():
    return int(input("Digite o saldo: "))

def pode_comprar(valor):
    return buscar_saldo() >= valor