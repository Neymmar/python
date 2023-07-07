from random import randint
computador = randint(0, 10)
print('Olá, sou seu computador...pensei em um número entre 0 e 10')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais')
        elif jogador > computador:
            print('menos')
print(f'Você acertou com {palpite} palpites')