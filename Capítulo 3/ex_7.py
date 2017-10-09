from ex_6 import bissexto

def dias_mes(mes, ano):
    mesCom31 = [
        'jan', 'mar', 'may',
        'jul', 'aug', 'oct',
        'dec'
    ]
    mesCom30 = [
        'apr', 'jun', 'sep',
        'nov'
    ]
    if mes in mesCom31:
        return 31
    elif mes in mesCom30:
        return 30
    elif mes == 'fev':
        if bissexto(ano):
            return 29
        return 28
    raise ValueError("Mes não existe")