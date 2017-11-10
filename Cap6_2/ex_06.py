def muda(fn, num):
    if num < 10:
        return fn(num)
    else:
        nn = fn(num % 10)
        return nn + 10 ** num_digitos(nn) * muda(fn, num // 10)

def num_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + num_digitos(n // 10)

def soma_dois(num):
    return muda(lambda x: x + 2, num)