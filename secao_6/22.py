nota = int(input("Digite uma nota de 10 a 20: \n"))

lista = []


while 10 <= nota <= 20:
    lista.append(nota)
    print("Próxima nota ")
    nota = int(input())
    if 10 > nota or nota > 20:
        print(f"A média aritmética das notas é {(sum(lista) / (len(lista)))}")

if len(lista) == 0:
    print("número fora dos parâmetros")
