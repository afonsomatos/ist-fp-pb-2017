ns = list(
    map(int,
        input("Escreva 3 numeros: ").split()
    )
)[:3]

print("O maior é {}".format(max(ns)))