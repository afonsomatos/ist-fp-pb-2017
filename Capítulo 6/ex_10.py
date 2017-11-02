def maior(lista):

    def percorre(n, max):
        if n > len(lista) - 1:
            return max
        if lista[n] > max:
            return percorre(n + 1, lista[n])
        else:
            return percorre(n + 1, max)

    return percorre(1, lista[0])