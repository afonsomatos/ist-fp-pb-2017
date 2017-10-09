def dia_int_str(n):
    if n == 0:
        return 'sabado'
    elif n == 1:
        return 'domingo'
    elif n == 2:
        return 'segunda'
    elif n == 3:
        return 'terça'
    elif n == 4:
        return 'quarta'
    elif n == 5:
        return 'quinta'
    elif n == 6:
        return 'sexta'

def chao(n):
    return n // 1

def dia_da_semana(dia, mes, ano):
    if 1 <= mes < 3:
        ano -= 1
        mes += 12

    K = ano % 100
    J = chao(ano/100)

    operacao = dia + \
        chao(13 * (mes + 1) / 5) + \
        K + \
        chao(K / 4) + \
        chao(J / 4) + \
        (- 2 * J)

    operacao %= 7

    return dia_int_str(operacao)