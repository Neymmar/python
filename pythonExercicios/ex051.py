# formula de razão
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c)
print('Acabou')