def soma_digitos_pares(n):
    resto   = n // 10
    digito  = n % 10
    somar   = 0

    if digito % 2 == 0:
        somar = digito

    if digito == 0:
        return somar

    return somar + soma_digitos_pares(resto)