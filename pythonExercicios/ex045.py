from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('==' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('==' * 10)
if computador == 0:
    if jogador == 0:
        print('Empatou !')
    elif jogador == 1:
        print('Jogador Ganhou !')
    elif jogador == 2:
        print('Computador ganhou !')
    else:
        print('Jogada invalida !')
elif computador == 1:
    if jogador == 1:
        print('Empatou !')
    elif jogador == 2:
        print('Jogador Ganhou !')
    elif jogador == 0:
        print('Computador ganhou !')
    else:
        print('Jogada invalida !')
elif computador == 2:
    if jogador == 2:
        print('Empatou !')
    elif jogador == 0:
        print('Jogador Ganhou !')
    elif jogador == 1:
        print('Computador ganhou !')
    else:
        print('Jogada invalida !')