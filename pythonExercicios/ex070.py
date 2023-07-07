print('==' * 15)
print('LOJA SUOER BARATO')
print('==' * 15)
altoPreco = total = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        altoPreco += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print('Fim do Programa')
print(f'O total da compra foi {total:.2f}')
print(f'{altoPreco} profutos custam mais de R$ 1000,00.')
print(f'O produto mais barato foi {barato}, que custa R$ {menor}')