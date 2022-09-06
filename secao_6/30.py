n = int(input("Insira um valor para N para ser calculado nas seguintes sequências\n"
              "1 + 2 + 3 + 4 + 5 + 6 +... + N\n"
              "1 - 2 + 3 - 4 + 5 + ...+ (2N - 1)\n"  # A pegadinha aqui é justamente o sinal de + antes da fórmula
              "1 + 3 + 5 + 7 +...+ (2N - 1)\n"
              "N = "))

soma1 = soma2 = soma3 = 0

for i in range(1, n + 1):
    soma1 = soma1 + i

print(soma1)

for i in range(1, n + 1):
    if i % 2 != 0:
        i = (i * 1)
        soma2 = soma2 + i
    if i % 2 == 0:
        i = i * -1
        soma2 = soma2 + i

print(f"{soma2 + ((2 * n) - 1)}")

for i in range(1, n, 2):
    soma3 = soma3 + i

print(f"{soma3 + ((2 * n) - 1)}")
