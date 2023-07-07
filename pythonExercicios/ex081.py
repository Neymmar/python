lista = []
while True:
        lista.append(int(input('Digite um número: ')))
        escolha = str(input('Quer continuar ? [S/N] '))
        if escolha in 'Nn':
                break
print('+=' * 30)
print(f'Foram digitados {len(lista)}')
if 5 in lista:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não foi digitado')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente foi {lista}')