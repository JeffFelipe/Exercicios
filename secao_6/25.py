from textwrap import wrap  # Importar essa biblioteca irá ajudar a formatar o resultado de forma "bonita", visualmente

n = 1000

lista = []

for i in range(1, n + 1):
    if i % 3 == 0:
        lista.append(i)
    elif i % 5 == 0:
        lista.append(i)

print("Os divisores de 3 e 5 entre 0 e 100 são:\n")
for lista in wrap(lista.__str__(), width=220):
    print(lista)
