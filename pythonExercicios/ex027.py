n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer !')
print('Seu primeiro nomeé ', nome[0])
print('Seu último nome é', nome[len(nome)-1])