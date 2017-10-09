x = int(input("Escreva um inteiro positivo\n? "))
invertido = 0

while x > 0:
    invertido = invertido * 10 + x % 10
    x = x // 10

print("O número invertido é ", invertido)