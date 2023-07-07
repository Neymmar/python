from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Nultiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opcao = int(input('Qual sua opção ? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'O resultado da soma de {n1} e {n2} é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O resultado da multiplicação de {n1} e {n2} é {mult}')
    elif opcao == 3:
        maior = n1
        if n1 < n2:
            maior = n2
            print((f'O maior número dentre os dois valores digitados é {maior}'))
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        print('Informe os novos valores')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando Programa...')
    else:
        print('Opção Invalida ! ...X...')
    print('==='*10)
    sleep(2)
print('Fim do programa !')