x = int(input("Qual o valor de x?\n "))
n = int(input("Qual o valor de n?\n "))
temp = 0
s = 0

while temp <= n:
    temp2 = 1
    fatorial = 1
    while temp2 <= temp:
        fatorial *= temp2
        temp2 += 1
    s += (x ** temp) / fatorial
    temp += 1

print("O valor da soma é ", s)