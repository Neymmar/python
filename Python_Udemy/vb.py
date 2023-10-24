palavra = 'dromedalho'
print('Bem vindo ao jogo da advinhação !')
print('-=' * 15)
print('DICA - É um animal.')
print('-=' * 15)
letra = str(input('Digite uma letra: '))
if palavra.count(letra) in palavra:
    print(letra)
else:
    print(f'Não tem a letra {letra} na palavra')