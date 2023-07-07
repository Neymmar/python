geral = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(geral) == 0:
        menor = maior = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    geral.append(pessoa[:])
    pessoa.clear()
    escolha = str(input('Quer continuar ? [S/N] '))
    if escolha in 'Nn':
        break
print(f'Você cadastrou {len(geral)} pessoas.')
print(f'O menor pesso foi de {menor}')
print(f'O maior peso foi de {maior}')