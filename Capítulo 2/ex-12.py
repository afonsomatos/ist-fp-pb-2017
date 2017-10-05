def fatorial(n):
    return 1 if n <= 1 else n * fatorial(n - 1)

x = int(input("Qual o valor de x?\n "))
n = int(input("Qual o valor de n?\n "))
temp = 0
s = 0

while temp <= n:
    s += (x ** temp) / fatorial(temp)
    temp += 1

print("O valor da soma é ", s)