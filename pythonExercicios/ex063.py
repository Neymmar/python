n = int(input('Quantos termos deseja na sequência de fibonacci ? '))
t1 = 0
t2 = 1
c = 3
print(f'{t1} -> {t2} -> ', end='')
while c <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    c += 1
    t1 = t2
    t2 = t3
print('Fim')