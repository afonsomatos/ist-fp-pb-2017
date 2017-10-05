numero = 0

while True:
    print("Escreva um dígito")
    print("(-1 para terminar)")
    x = int(input("? "))
    if x < 0:
        break
    numero = numero * 10 + x

print("O número é: ", numero)