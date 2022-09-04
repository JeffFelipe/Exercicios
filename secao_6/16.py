print("Digite um número positivo ímpar.\n")

n = int(input())

if n > -1:
    if n % 2 != 0:
        lista = list(range(1, (n + 2), 2))

        print(f"Os números ímpares de 0{n} a 0 são:\n{lista[::-1]}")
    else:
        lista = list(range(1, (n + 1), 2))

        print(f"Os números ímpares de {n} a 0 são:\n{lista[::-1]}")
else:
    print("Número negativo: fora dos parâmetros")
