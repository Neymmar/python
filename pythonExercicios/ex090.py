aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['nota'] = float(input('Nota: '))
if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado !'
elif 5 <= aluno['nota'] < 7:
    aluno['situação'] = 'Na Média !'
else:
    aluno['situação'] = 'Reprovado !'
for k, v in aluno.items():
    print(f'    - {k} é igual a {v}')