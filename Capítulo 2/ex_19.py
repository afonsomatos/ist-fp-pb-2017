x = float(input("Quantia em euros: "))
c = int(x * 10 * 10) # usar (*100) causa erros de precisao

print(c)

notas = {
    "Notas 50€": 50 * 100,
    "Notas 20€": 20 * 100,
    "Notas 10€": 10 * 100,
    "Notas 5€": 5 * 100,
    "Moedas 2€": 200,
    "Moedas 1€": 100,
    "Moedas 50c": 50,
    "Moedas 20c": 20,
    "Moedas 10c": 10,
    "Moedas 5c": 5,
    "Moedas 2c": 2,
    "Moedas 1c": 1
}

for i, v in notas.items():
    print(i, " - ", c // v)
    c %= v