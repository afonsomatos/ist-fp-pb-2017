x = int(input("Escreva um número\n-> "))
normal = x
invertido = 0
p = 0

while x > 0:
    invertido = invertido * 10 + x % 10
    x = x // 10
    p += 1

resultado = normal * (10 ** p) + invertido
print(resultado)
