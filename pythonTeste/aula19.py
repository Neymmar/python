escritorio = []
departamento1 = {'nome': 'Neymmar', 'idade': 27, 'sexo': 'M'}
departamento2 = {'nome': 'Leticia', 'idade': 23, 'sexo': 'F'}
escritorio.append(departamento1)
escritorio.append(departamento2)
print(f'{departamento1["nome"]} tem {departamento1["idade"]} anos.')
print(departamento1.keys())
print(departamento1.values())
print(departamento1.items())
print('======================')
print(f'{departamento2["nome"]} tem {departamento2["idade"]} anos.')
print(departamento2.keys())
print(departamento2.values())
print(departamento2.items())
print('======================')
print(escritorio)
print('======================')
print(escritorio[1]['nome'])