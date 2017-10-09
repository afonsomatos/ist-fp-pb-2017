while True:
    print("Escreva um número de segundos")
    print("(um número negativo para terminar)")
    x = int(input("? "))
    if x < 0:
        break
    d = x / (60 * 60 * 24)
    print("O número de dias correspondente é ", d)



