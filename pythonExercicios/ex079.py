escolha = 'SsNn'
valor = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
    else:
        print('Valor já digitado !')
    escolha = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if escolha in 'n':
        break
valor.sort()
print(f'Os valores inseridos foram {valor}')