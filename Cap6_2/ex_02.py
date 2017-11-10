def filtra(tst, lst):
    if lst == []:
        return []
    if tst(lst[0]):
        return [lst[0]] + filtra(tst, lst[1:])
    return filtra(tst, lst[1:])

def transforma(fn, lst):
    if lst == []:
        return []
    return [fn(lst[0])] + transforma(fn, lst[1:])

def acumula(fn, lst):
    if len(lst) == 1:
        return lst[0]
    return fn(lst[0],
              acumula(fn, lst[1:])
              )