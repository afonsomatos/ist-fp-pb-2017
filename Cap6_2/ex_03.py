from Cap6_2 import ex_02

def soma_quadrados_impares(lst):
    return ex_02.acumula(
        lambda x, y: x * x + y,
        ex_02.filtra(lambda x: x % 2 != 0, lst) + [0]
    )

print(
    soma_quadrados_impares([1,2,3])
)