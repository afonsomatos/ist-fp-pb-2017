x = int(input("Escreva um numero inteiro: "))
s = 0

while x > 0:
    s += x % 10
    x = x // 10

print("Soma dos digitos: ", s)