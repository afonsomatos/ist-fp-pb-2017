s  = int(input("Escreva o número de segundos "))

ms = 60
hs = ms * 60
ds = hs * 24

d = s // ds
s %= ds
h = s // hs
s %= hs
m = s // ms
s %= ms

print("dias: {} horas: {} mins: {} segs: {}".format(
    d, h, m, s
))