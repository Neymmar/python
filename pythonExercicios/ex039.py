from datetime import date
nasc = int(input('Em que ano você nasceu: '))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    print(f'Você ainda não precisa, só daqui a {18 - idade} anos alistar !')
elif idade > 18:
    print(f'Você já devia ter se alistado a {idade - 18} anos')
else:
    print('Você está no ano do alistamento')