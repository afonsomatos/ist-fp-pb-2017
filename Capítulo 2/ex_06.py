a, b, c = input("Escreva 3 números: ").split()
a = int(a)
b = int(b)
c = int(c)

maior = c

if b < a > c:
    maior = a
elif c < b > a:
    maior = b

print("O maior é ", maior)