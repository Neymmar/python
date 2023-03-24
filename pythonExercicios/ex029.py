vel = float(input('Qual sua velocidade: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Você está dentro do limite de velocidade !')
else:
    print('Você está acida do limite permitido na via q é de 80km/h ! MULTADO')
    print(f'Você dever pagar uma multa de R${multa:.2f}')