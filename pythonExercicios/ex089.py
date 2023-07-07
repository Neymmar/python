pessoas = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    pessoas.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print('-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i,a in enumerate(pessoas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')