def nenhum_p(n, p):
    if n == 1:
        return not p(n)
    return (not p(n)) or nenhum_p(n - 1, p)