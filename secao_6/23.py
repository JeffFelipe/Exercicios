print("Digite um número positivo")

num = int(input())

i = 1

divisores = []

if num < 0:
    num = int(input('Digite um número positivo: '))

for i in range(i, num+1):
    if num % i == 0:
        divisores.append(i)

print(f"Os divisores de {num} são {divisores}")
