nome = str(input('Nome: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura * altura)
print(f'{nome}, tem {altura} de altura, pesa {peso}Kg, e seu IMC é {imc:.2f}')