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
    for numero in range(valor1, valor2 + 1):  # Para elemento(numero) dentro do range a seguir
        if numero % 2 == 0:  # Se esse elemento tiver resto 0 na divisão por 2
            par += numero  # Esse número é par então será somado com os elementos de numero
        else:
            impar *= numero  # Se não, é impar e será multiplicado com os elementos de numero
    print(f'A soma de todos os pares é: {par}\nA multiplicação de todos os ímpares é: {impar}')
    break

