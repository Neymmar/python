from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador escolher um número aleatório de 0 a 5
print('===' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar')
print('===' * 20)
numero = int(input('Qual número você acha que eu pensei ? '))
print('Processando...')
sleep(2)
if numero == computador:
    print('Parabéns, você acertou !')
else:
    print(f'Que pena você errou, em pensei no número {computador}')