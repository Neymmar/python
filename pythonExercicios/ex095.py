time = list()
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador ? '))
    totPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    partidas.clear()
    for c in range (1, totPartidas + 1):
        partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('Digite apenas S ou N.')
    if resp in 'N':
        break
print('==' * 20)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('==' * 20)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('==' * 20)