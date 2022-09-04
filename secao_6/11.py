print("Digite um número inteiro positivo")

n = int(input())
if n > -1:
    lista = list(range(0, (n + 1), 1))

    print(f"Os números naturais de 0 a {n} são:\n{lista}")
