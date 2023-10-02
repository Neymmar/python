def area(l, c): 
    a = l * c
    print(f'A área de um terreno {l}x{c} é {a}m².')


print('Controel de Terrenos')
print('==' * 10)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
