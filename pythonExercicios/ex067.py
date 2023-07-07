while True:
    val = int(input('Quer ver a tabuada de qual valor ? '))
    if val < 0:
        break
    print('+='*15)
    for cont in range (1,11):
        equa = val * cont
        print(f'{val} X {cont} = {equa}')
    print('+='*15)
print('Programa encerrado !')