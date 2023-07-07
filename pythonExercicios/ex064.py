cont = soma = numero = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    soma += numero
    cont += 1
print(f'Você digitou {cont-1} números, e soma deles foi {soma - 999} ')