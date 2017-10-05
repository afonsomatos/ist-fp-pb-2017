n = 1
ac = 0

while n <= 9:
    ac = ac * 10 + n
    r = ac * 8 + n
    print(ac, "x 8 +", n, "=", r)
    n += 1