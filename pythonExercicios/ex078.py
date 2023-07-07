valores = []
menor = maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if menor > valores[c]:
            menor = valores[c]
        if maior < valores[c]:
            maior = valores[c]
print('-='*15)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()