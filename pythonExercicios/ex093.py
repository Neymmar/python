jogador = {}
partidas = []
jogador['nome'] = str(input('Qual o nome do jogador ? '))
totPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range (1, totPartidas + 1):
    partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('==' * 20)
print(jogador)
print('==' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('==' * 20)
print(f'o jogador {jogador["nome"]} jogou {totPartidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'{jogador["nome"]} fez um total de {sum(partidas)}')
