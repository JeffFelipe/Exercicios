print("Digite um número inteiro qualquer.\n")

ni = []

adiciona = int(input())

if adiciona % 2 != 0:
    while len(ni) < 10:
        ni.append(adiciona + 2)
        adiciona = adiciona + 2
else:
    while len(ni) < 10:
        ni.append(adiciona + 1)
        adiciona = adiciona + 1

print(f"Os próximos 10 números naturais ímpares são:\n{ni}")

"""
CÓDIGO COMENTADO

print("Digite um número inteiro qualquer.\n")

ni = []  # criei uma lista sem nenhum valor

adiciona = int(input())  # campo para usuário inserir o número

if adiciona % 2 != 0:  # Se a variável adiciona dividida por 2 e tiver como resto diferente de 0
    while len(ni) < 10:  # Enquanto o len da lista ni for menor que 10 índice
        ni.append(adiciona + 2)  # irá inserir na lista ni o valor inicial de adiciona + 2
        adiciona = adiciona + 2  # modifica o valor de adiciona, criando o looping
else:  # Se não
    while len(ni) < 10:
        ni.append(adiciona + 1)
        adiciona = adiciona + 1

print(f"Os próximos 10 números naturais ímpares são:\n{ni}")
"""