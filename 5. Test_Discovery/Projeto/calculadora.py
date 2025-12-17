def media(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Erro! Valor diferente de número identificado")
    return (a + b) / 2
