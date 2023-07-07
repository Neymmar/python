lista = []
par = []
impar = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
    if n % 2 == 1 in lista:
        impar.append(n)
    else:
        par.append(n)
print('=+' * 15)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
