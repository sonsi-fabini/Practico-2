def filtrar_pares(numeros):
    """Devuelve una lista con los números pares"""
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares



