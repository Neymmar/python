from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogaror4': randint(1, 6)}
rank = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.6)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('==' * 13)
print('==RANKING DOS JOGADORES==')
for i, v in enumerate(rank):
    print(f'O {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.6)