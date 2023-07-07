lista = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<29}', end=' ')
    else:
        print(f'R$ {lista[posicao]:>7.2f}')
print('-' * 40)
