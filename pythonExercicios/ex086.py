princ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        princ[l][c] = int(input(f'Digite um valor para  a posicão [{l},{c}] para uma matrix de 3x3: '))
print('+=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{princ[l][c]:^5}]', end='')
    print()
