fracao = 0
harmonica = 0

num = int(input(f'Digite um número: '))

for num in range(0, num + 1):
    if num > 0:
        fracao = 1 / num
        harmonica += fracao

print(f'O valor de H({num}) é {harmonica:.2f}')  # o comando .2f é apenas de formatação, faz com q o Python me retorne
# apenas dois dígitos após o "."
