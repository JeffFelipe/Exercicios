print("Digite dez números")

num = []  # criei uma lista vazia

while len(num) < 10:  # Enquanto num tiver menos que 11 índices
    adiciona = float(input())  # Adiciona um inteiro
    num.append(adiciona)  # Adiciona o elemento a lista

print(f"O maior valor digitado é {max(num)}")
print(f"O menor valor digitado é {min(num)}")
