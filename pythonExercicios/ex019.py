import random
alu1 = str(input('Digite o nome do primeiro aluno: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
lista = [alu1, alu2, alu3,alu4]
escolha = random.choice(lista)
print(f'O aluno escolhido foi {escolha}')