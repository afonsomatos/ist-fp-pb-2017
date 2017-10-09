x = int(input("Escreva um inteiro\n? "))
r = 0
p = 0

while x > 0:
    d = x % 10
    x = x // 10
    if d % 2 != 0:
        r += d * (10 ** p)
        p += 1

print("Resultado: ", r)