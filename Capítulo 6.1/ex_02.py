def apenas_digitos_impares(n):
    digito  = n % 10
    resto   = n // 10

    if digito % 2 != 0:
        if resto == 0:
            return digito
        return apenas_digitos_impares(resto) * 10 + digito

    if resto == 0:
        return 0

    return apenas_digitos_impares(resto)