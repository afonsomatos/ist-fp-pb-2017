def troca_occ_lista(lista, a, b):
    if len(lista) == 0:
        return []

    el = lista[0]
    novo_el = el

    if el == a:
        novo_el = b

    return [novo_el] + troca_occ_lista(lista[1:], a, b)
