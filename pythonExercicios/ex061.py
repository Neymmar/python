# formula de razão
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    c += 1
print('Acabou')
