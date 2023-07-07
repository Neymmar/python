from datetime import date
nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - nasc
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM !')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL !')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é JUNIOR !')
elif idade <= 25:
    print(f'Você tem {idade} anos e sua categoria é SÊNIOR !')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER !')