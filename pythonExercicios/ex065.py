soma = media = cont = maior = menor = 0
escolha = 'S'
while escolha == 'S':
    num = int(input('Digite um número: '))
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número digitado foi {maior}, e o menor foi {menor}')