def area_circulo(valor):
    return valor * valor * 3.14

def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError("r1 maior que r2")
    else:
        return area_circulo(r2) - area_circulo(r1)