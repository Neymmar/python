lista = []
impar = []
par = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    escolha = str(input('Quer continuar ? [S/N] '))
    if escolha in 'Nn':
        break
print(f'Todos os valores digitados: {lista}')
print(f'Os valores ímpares digitas: {impar}')
print(f'Os valores pares digitados: {par}')
