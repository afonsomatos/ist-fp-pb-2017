lista = input("Notas dos alunos: ").split()

positivas = 0
n = 0
while n < len(lista):
    if int(lista[n]) >= 10:
        positivas += 1
    n += 1

percentagem = positivas * 100 / len(lista)

print("Positivas: ", positivas, " % ->", percentagem)