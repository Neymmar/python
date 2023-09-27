real = float(input('Valor a ser convertido: R$'))
dolar = float(input('Cotação atual do dolar: U$'))
valor = real / dolar
print(f'Com R${real} você terá U${valor:.2f} em dolares.')