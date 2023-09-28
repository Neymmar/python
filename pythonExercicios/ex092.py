from datetime import datetime
dados = {}
dados['nome'] = str(input('Qual seu nome: '))
nasc = int(input('Em que ano você nasceu ? '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('==' * 20)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')