from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print('¬¬' * 20)
print('     JOGAR NA MEGA SENA        ')
print('¬¬' * 20)
resp = int(input('Quantos jogos você quer que sorteie ? '))
while tot <= resp:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-' * 3, f'Sorteando {resp} JOGOS ', '=-' * 3)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('¬¬¬¬        BOA SORTE         ¬¬¬¬')