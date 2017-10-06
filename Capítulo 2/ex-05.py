from math import sqrt

a, b, c, d, e = input("Escreva 5 números: ").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

media = (a + b + c + d + e) / 5

delta = 0
delta += (a - media) ** 2
delta += (b - media) ** 2
delta += (c - media) ** 2
delta += (d - media) ** 2
delta += (e - media) ** 2

desvio = sqrt(0.25 * delta)

print("Média: {} Desvio: {}".format(media, desvio))
