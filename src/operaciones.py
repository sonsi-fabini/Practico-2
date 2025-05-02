def filtrar_pares(numeros):
    """Devuelve una lista con los números pares"""
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares

def filtrar_impares(numeros):
    """Devuelve una lista con los números impares"""
    impares = []
    for i in numeros:
        if i % 2 != 0:
            impares.append(i)
    return impares
