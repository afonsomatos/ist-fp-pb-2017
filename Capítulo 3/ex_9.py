def serie_geom(r, n):
    if not type(r) is int:
        raise ValueError("r errado")
    elif not type(r) is int or n < 0:
        raise ValueError("n errado")

    soma = 0
    for x in range(0, n + 1):
        soma += r ** x
    return soma