def soma_n_vezes(a, b, n):
    if n == 0:
        return b
    return a + soma_n_vezes(a, b, n - 1)