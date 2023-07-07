n = int(input('Qual número você deseja saber a tabuada: '))
for c in range (1, 11, +1):
    print(f'{n} x {c:2} = {c * n}')