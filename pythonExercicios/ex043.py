print('==' * 6)
print('Calculo IMC')
print('==' * 6)
alt = float(input('Altura: '))
peso = float(input('Peso Kg: '))
imc = peso / (alt ** 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Abaixo do Peso !')
elif imc < 25:
    print('Peso ideal !')
elif imc < 30:
    print('Sobrepeso !')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida !')