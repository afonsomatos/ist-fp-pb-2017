def sublistas(lista):
    if len(lista) == 0:
        return 0
    if type(lista[0]) == list:
        return 1 + sublistas(lista[0]) + sublistas(lista[1:])
    return sublistas(lista[1:])