x = int(input("Escreva um inteiro\n? "))
zeros = 0

while x > 0:
    d1 = x % 10
    d2 = x % 100
    if d1 == 0 and d2 == 0:
        zeros += 1
    x = x // 10

print("O numero tem ", zeros, " zeros seguidos")