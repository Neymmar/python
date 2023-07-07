print('__' * 15)
print('CADASTRE UMA PESSOA')
print('__' * 15)
homem = mulherMen = mulherTot= menor = maior = 0
while True:
    idade = int(input('Idade: '))
    if idade < 18:
        menor += 1
    else:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        mulherTot += 1
    if sexo == 'F' and idade < 20:
        mulherMen += 1
    print('__' * 15)
    escolha = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Maiores de Idade {maior}, menores de idade {menor}, mulheres no total {mulherTot}, homens no total {homem} mulheres menores de idade {mulherMen}')