horas = int(input("Número de horas trabalhadas na semana: "))
ganho = int(input("Salário por hora: "))

pagamento = horas * ganho

if horas > 40:
    pagamento += ganho * 2 * (horas - 40)