def calcularDinheiro(valor):
    valor = int(valor * 10 * 10)

    itens = (
        ("Nota 50€", 50 * 100),
        ("Nota 20€", 20 * 100),
        ("Nota 10€", 10 * 100),
        ("Nota 5€", 5 * 100),
        ("Moeda 2€", 200),
        ("Moeda 1€", 100),
        ("Moeda 50 cêntimos", 50),
        ("Moeda 20 cêntimos", 20),
        ("Moeda 10 cêntimos", 10),
        ("Moeda 5 cêntimos", 5),
        ("Moeda 2 cêntimos", 2),
        ("Moeda 1 cêntimo", 1)
    )

    for t in itens:
        quantia = valor // t[1]
        valor %= t[1]
        print(t[0], "-", quantia)