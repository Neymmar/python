n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 < n2:
    print(f'O primeiro valor digitado {n1} é menor que o segundo valor digitado {n2}')
elif n2 < n1:
    print(f'O segundo valor digitado {n2} é menor que o primeiro valor digitado {n1}')
else:
    print('Os valores digitados são iguais')    