from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Em que ano você nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'No total tivemos {maior} pesoas maior de idade, e {menor} pesoas menor de idade')