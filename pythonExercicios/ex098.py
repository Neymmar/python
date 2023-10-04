from time import sleep


def cont(ini, fim, pas):
    if pas < 0:
        pas *= 1
    if pas == 0:
        pas = 1
    print('==' * 15)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(2.5)
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += pas
        print('FIM !')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= pas
        print('FIM !')


cont(1, 10, 1)
cont(10,0,2)
print('==' * 15)
print('Agora é a sua vez de personalizar a contagem !')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)