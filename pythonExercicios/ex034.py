sal = float(input('Qual seu salário atual ? R$'))
if sal <= 1250:
    novo = sal + sal * 0.15
    print(f'Seu salário passara a ser {novo:.2f}, com um aumento de 15%')
else:
    novo = sal * 0.1
    print(f'Seu salário passara a ser {novo:.2f}, com um aumento de 10%')