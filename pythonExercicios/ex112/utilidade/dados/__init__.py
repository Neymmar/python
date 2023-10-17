def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRo: \"{entrada}"\ é um preço inválido')
        else:
            entrada = True
            return float(entrada)