def inverte(lista):
    if len(lista) <= 1:
        return lista
    return [lista[-1]] + inverte(lista[0:-1])