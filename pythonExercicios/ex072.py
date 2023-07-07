num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolha = int(input('Qual número deseja saber por extenso ? '))
    if escolha > 20:
        print('Número inválido, tente novamente')
    else:
        break
print(f'O número {escolha} por extenso é {num[escolha]}.')