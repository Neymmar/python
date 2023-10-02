def linha(msg):
    print('==' * 15)
    print(msg)


def cont(a,b, c):
    for i in range(a, b, c):
        print(i, end=' ')


linha('Contagem de 1 até 10 de 1 em 1')
cont(0, 10, 1)
linha('Contagem de 10 até 0 de 2 em 2')
cont(10,0,-2)