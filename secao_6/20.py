print("Digite números aleatórios, quando terminar, digite 1000 para sair")

num = []

adiciona = int(input())

pares = []

if adiciona % 2 == 0:
    print("par")
elif adiciona % 2 != 0:
    print("impar")
if adiciona == 1000:
    print("Você digitou 1000 para sair")

while adiciona != 1000:
    num.append(adiciona)
    adiciona = int(input())
    if adiciona % 2 == 0:
        print("par")
        pares.append(adiciona)
    if adiciona % 2 != 0:
        print("impar")
else:
    print(f"O número de dados lidos foi {len(num)}")
    print(f"O número de valores pares foi {len(pares)}")
    print(pares)


