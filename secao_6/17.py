print("Insira um número inteiro positivo qualquer\n")

num = int(input())
soma = []

if num > -1:
    soma = list(range(0, num, 1))
    print(f"A soma dos {num} primeiros naturais é naturais é {sum(soma)}")
else:
    print("Número fora dos parâmetros")
