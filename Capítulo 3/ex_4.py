from ex_3 import area_circulo

def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError("r1 maior que r2")
    else:
        return area_circulo(r2) - area_circulo(r1)