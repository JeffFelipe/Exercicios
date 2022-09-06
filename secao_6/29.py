from math import factorial

f = 1

numerador = 0

n = 0

cont = 1

s = 0

while cont <= 5:
    n = n + 2
    f = factorial(n)
    numerador = numerador + 1
    s = (numerador / f) + s
    cont = cont + 1


print(f"o valor final de S é: {s}")
