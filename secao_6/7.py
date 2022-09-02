print("Digite dez números inteiros")

num = []  # criei uma lista vazia

while len(num) < 10:  # Enquanto num tiver menos que 11 índices
    adiciona = int(input())  # Adiciona um inteiro
    if adiciona > -1:  # Se maior que o negativo -1
        num.append(adiciona)  # Adiciona o elemento a lista

print(f"A média total desses valores é {sum(num) / 10}")
