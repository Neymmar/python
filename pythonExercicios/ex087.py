princ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaCol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        princ[l][c] = int(input(f'Digite um valor para  a posicão [{l},{c}] para uma matrix de 3x3: '))
        if princ[l][c] % 2 == 0:
            somaPar += princ[l][c]
print('+=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{princ[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    somaCol =+ princ[l][2]
for c in range(0, 3):
    if c == 0:
        maior = princ[1][c]
    elif princ[1][c] > maior:
        maior = princ[1][c]
print('+=' * 30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaCol}')
print(f'O maior valor digitado na segunda linha foi {maior}')
