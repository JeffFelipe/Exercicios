print("Insira um número entre 100 e 999")

num = int(input())

if 99 < num < 1000:
    x = [int(a) for a in str(num)]
    print(x)
else:
    print("Número fora do parâmetro")
