dis = float(input('Qual a distância da sua viagem em km ? '))
if dis <= 200:
    print('O valor a ser pago é de R$', (dis * 0.5))
else:
    print('O valor a ser pado é de R$', (dis * 0.45))