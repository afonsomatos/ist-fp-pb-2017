from Cap6_2 import ex_02

def junta_listas(lstl):
    return ex_02.acumula(lambda x, y: x + y, lstl)


print(
    junta_listas([[1, 2], [[3]], [4, 5]])
)