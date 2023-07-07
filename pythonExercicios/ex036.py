print('=='* 6)
print('Empréstimo !')
print('=='* 6)
casa = float(input('Qual o valor da casa que você deseja ? R$'))
salario = float(input('Quanto você recebe de salário ? R$'))
anos = int(input('Pretende pagar essa casa em quantos anos ? '))
meses = anos * 12
prestacao = casa / meses
minimo = salario * 30 / 100
print(f'Uma casa no valor de {casa:.2f}, a ser paga por {anos} anos. O valor da prestação será de {prestacao:.2f}')
if prestacao >= minimo:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')