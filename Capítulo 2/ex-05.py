from math import sqrt

numeros = list(
    map(int,
        input("Escreva 5 números: ").split()))[:5]

media = sum(numeros) / len(numeros)
desvio = sqrt(0.25 * sum([(x - media) ** 2 for x in numeros]))

print("Média: {} Desvio: {}".format(media, desvio))