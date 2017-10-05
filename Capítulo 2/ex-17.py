lista = input("Notas dos alunos: ").split()
positivas = sum([1 if int(x) >= 10 else 0 for x in lista])
percentagem = positivas * 100 / len(lista)

print("Positivas: ", positivas, " % ->", percentagem)