from random import randint

numeros = list()
for cont in range (0, 5):
    numeros.append(randint(1, 10))
print(numeros)
soma = 0
for valor in numeros:
    if valor % 2 == 0:
        soma += valor
print(f'A soma de todos os números pares sorteados foi {soma}.')