ni = []
adiciona = 0

if adiciona % 2 == 0:
    while len(ni) < 50:
        ni.append(adiciona + 2)
        adiciona = adiciona + 2

print(f"Os cinquenta primeiros pares são\n{ni}\n"
      f"A soma dos cinquenta primeiros pares é {sum(ni)}")
