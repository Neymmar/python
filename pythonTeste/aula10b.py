n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'A média da sua nota foi {media:.2f}')
if media >= 7:
    print('Você foi aprovado !')
else:
    print('Você foi reprovado !')