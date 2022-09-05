print("Digite um número")

n = int(input())

for i in range(n + 1, n + 18):  # Pala elemento i no range de n + 1(Isso faz q o range inicie após o N, com final de n
    # + 18 ( fazendo q o limite do range seja o 17
    if i % 11 == 0:
        div_11 = i
        print(f'O primeiro múltiplo de 11 após {n} é  {div_11} ')

    if i % 13 == 0:
        div_13 = i
        print(f'O primeiro múltiplo de 13 após {n} é {div_13} ')

    if i % 17 == 0:
        div_17 = i
        print(f'O primeiro múltiplo de 17 após {n} é {div_17} ')
        break

