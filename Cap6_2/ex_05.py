def concentra(op, num):
    if num < 10:
        return num
    else:
        return op(num % 10, concentra(op, num // 10))

def produto(num):
    return concentra(lambda d, r: d * r, num)