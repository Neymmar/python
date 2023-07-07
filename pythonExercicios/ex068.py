from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o tatal deu {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu')
        else:
            printa('Você perdeu')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você venceu')
        else:
            printa('Você perdeu')
            break
