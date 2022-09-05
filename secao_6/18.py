print("Insira quantos números deseja analisar")

num = []
quantidade = int(input())

while len(num) < quantidade:
    adiciona = int(input())
    num.append(adiciona)

print(f"O maior dos número escolhidos é {max(num)} e ele foi inserido {num.count(max(num))} vezes")
