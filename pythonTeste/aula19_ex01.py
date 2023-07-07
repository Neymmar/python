estado = dict() ## dicionários podem ser escrito apenas com {} também
brasil = list() ## lista podem ser escrito apenas com () também
for c in range(0, 3):
    estado['estado'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
