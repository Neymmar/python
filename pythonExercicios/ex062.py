# formula de razão
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
r = 10
total = 0
while r != 0:
    total = total + r
    while c <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        c += 1
    print('Pausa')
    r = int(input('Quantos você quer mostrar a mais ? '))
print('Acabou')
