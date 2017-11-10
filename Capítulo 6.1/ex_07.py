def pertence(lista, el):
    if len(lista) == 0:
        return False

    if lista[0] == el:
        return True

    return pertence(lista[1:], el)