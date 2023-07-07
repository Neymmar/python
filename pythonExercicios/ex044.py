compra = float(input('Valor da compra: R$ '))
print('''Qual a forma de pagamento ?
[1] À vista dinheiro/cheque com 10% de desconto
[2] À vista cartão com 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] Em 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Escolha: '))
if escolha == 1:
    total = compra - (compra * 10 / 100)
elif escolha == 2:
    total = compra - (compra * 5 / 100)
elif escolha == 3:
    total = compra
elif escolha == 4:
    total = compra + (compra * 20 / 100)
    print(f'O valor da sua compra de {compra}, sairá por {total}')
else:
    total = 0
    print('Opção invalida de pagamento ! Tente novamente')

