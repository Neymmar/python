n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operador = input('Digite o operador q deseja para fazer a conta [+-/*]: ')
if operador == '+':
    print(f'O número {n1} + {n2} = {n1 + n2}')
elif operador == '-':
    print(f'O número {n1} - {n2} = {n1 - n2}')
elif operador == '/':
    print(f'O número {n1} / {n2} = {n1 / n2}')
elif operador == '*':
    print(f'O número {n1} * {n2} = {n1 * n2}')
