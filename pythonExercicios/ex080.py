valor = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valor[-1]:
        valor.append(n)
    else:
        posicao = 0
        while posicao < len(valor):
            if n <= valor[posicao]:
                valor.insert(posicao, n)
                break
            posicao += 1
valor.sort()
print(f'Os valores digitados em ordem foram {valor}')