print("Digite um número inteiro positivo par.\n")

n = int(input())
if n > -1:
    if n % 2 == 0:
        lista = list(range(0, (n + 1), 2))

        print(f"Os números pares de {n} a 0 são:\n{lista[::-1]}")
    else:
        print("Número ímpar: fora dos parâmetros")
else:
    print("número negativo: fora dos parâmetros")
