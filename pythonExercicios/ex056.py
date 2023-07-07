somaIdade = 0
homem = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulherMenor = 0
for c in range(1,5):
    print(f'===== {c}ª PESSOA =====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo == 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherMenor += 1
mediaTot = somaIdade / 4
print(f'A média de idade do grupo é de {mediaTot} anos')
print(f'O homem mais velho se chama {nomeVelho}, e ele tem {maiorIdadeHomem} anos de idade')
print(f'Ao todo tem {mulherMenor} mulheres menor de 20 anos de idade')