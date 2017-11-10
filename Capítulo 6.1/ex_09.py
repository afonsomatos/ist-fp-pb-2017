def compara(lista, n, menor):
    if len(lista) == 0:
        return []

    el  = lista[0]
    dif = el - n

    if dif >= 0 and menor or dif < 0 and not menor:
        return compara(lista[1:], n, menor)

    return [el] + compara(lista[1:], n, menor)

def parte(lista, n):

    return [compara(lista, n, True),
            compara(lista, n, False)]