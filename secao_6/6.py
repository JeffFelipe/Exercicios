print("Digite abaixo dez número aleatórios")

num = []

while len(num) < 10:
    num.append(int(input()))

print(f"A média total desse valores é {sum(num)/ 10}")
