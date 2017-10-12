def calcularDinheiro(valor):
    valor = int(valor * 10 * 10)

    itens = (
        (50, 50 * 100, "Nota"),
        (20, 20 * 100, "Nota"),
        (10, 10 * 100, "Nota"),
        (5, 5 * 100, "Nota"),
        (2, 200, "Moeda"),
        (1, 100, "Moeda"),
        (50, 50, "Moeda"),
        (20, 20, "Moeda"),
        (10, 10, "Moeda"),
        (5, 5, "Moeda"),
        (2, 2, "Moeda"),
        (1, 1, "Moeda")
    )

    for t in itens:
        quantia = valor // t[1]
        valor %= t[1]
        print(t[2], "de", t[0], "-", quantia)


calcularDinheiro(50.55)