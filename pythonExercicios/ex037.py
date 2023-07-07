num = int(input('Digite um número inteiro que deseja ser convertido: '))
print('''Quer que converta pra binário, hexadecimal ou octal ?
[1] Binário
[2] Hexadecimal
[3] Octal ''')
escolha = int(input('Escolha: '))
if escolha == 1:
    print(f'{num} convertido em Binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido em Hexadecimal é {hex(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido em Octal é {oct(num)[2:]}')
else:
    print('O número digitado é invalido')