def subtrai(lista1, lista2):
    if len(lista1) == 0:
        return []
    if lista1[0] in lista2:
        return subtrai(lista1[1:], lista2)
    return [lista1[0]] + subtrai(lista1[1:], lista2)