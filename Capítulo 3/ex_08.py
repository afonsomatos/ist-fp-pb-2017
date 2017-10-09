def valor(q, j, n):
    if not type(q) is int or q <= 0:
        raise ValueError("q inválido")
    elif not 0 < j < 1:
        raise ValueError("j inválido")
    elif not type(n) is int or n <= 0:
        raise ValueError("n inválido")
    return q * ((1 + j) ** n)

def duplicar(q, j):
    n = 1
    while True:
        new_q = valor(q, j, n)
        if new_q >= 2 * q:
            return n
        n += 1