d = int(input("Introduza uma distância percorrida (km): "))
t = int(input("Introduza o tempo necessário para a percorrer (min): "))

kmh = d / (t / 60)
ms = (d * 1000) / (t * 60)

print("Velocidade média é {} Km / h ou {} m / s".format(kmh, ms))