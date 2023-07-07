print('===' * 10)
print('Analisando triângulos')
print('===' * 10)
pri = float(input('Primeiro valor: '))
seg = float(input('Segundo valor: '))
ter = float(input('Terceiro valor: '))
if pri < seg + ter and seg < pri + ter and ter < pri + seg:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
    if pri == seg == ter:
        print('Esse triângulo é Equilátero !')
    elif pri != seg and seg != ter and ter != pri:
        print('Esse triângulo é Escaleno !')
    elif pri == seg or seg == ter or ter == pri:
        print('Esse triângulo é Isósceles !')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')