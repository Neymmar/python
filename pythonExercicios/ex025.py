'''
só irá considerar como true as pessoas que tiverem silva no nome
'''
nome = str(input('Qual seu nome completo: ')).strip()
print('Seu nome tem Silva ?', 'silva' in nome.lower())

