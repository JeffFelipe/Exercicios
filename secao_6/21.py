print("Escreva abaixo dois números abaixo")

valor1 = int(input("Primeiro "))
valor2 = int(input("Segundo "))

par = 0
impar = 1

lista = list(range(valor1, valor2 + 1))

while valor1 > valor2:
    print("Insira os valores do menor para o maior")
    break

while valor1 < valor2:
    for numero in range(valor1, valor2 + 1):
        if numero % 2 == 0:
            par += numero
        else:
            impar *= numero
    print(f'A soma de todos os pares é: {par}\nA multiplicação de todos os ímpares é: {impar}')
    break

