geral = []
pessoas = {}
totPess = soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('Digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    geral.append(pessoas.copy())
    totPess += 1
    soma += pessoas['idade']
    while True:
        continuar = str(input('Gostaria de cadastrar outra pessoas[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Digite apenas S ou N.')
    if continuar in 'N':
        break
media = soma / totPess
print('==' * 20)
print(f'A) Ao todo temos {totPess} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for m in geral:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média ', end='')
for ac in geral:
    if ac['idade'] > media:
        print(f'{ac["nome"]}', end='')