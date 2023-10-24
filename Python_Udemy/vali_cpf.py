# Primeiro Digito
import re
entrada = input('Digite seu CPF: ')
cpf_usuario = re.sub(r'[^0-9]', '', entrada)
nove_digitos = cpf_usuario[:9]
contador_regressivo = 10
resultado_digito = 0
for digito in nove_digitos:
    resultado_digito += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito * 10) % 11
if digito_1 <= 9:
    digito_1 = digito_1
else:
    digito_1 = 0
# Segundo Digito
dez_digitos = nove_digitos + str(digito)
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
if digito_2 <= 9:
    digito_2 = digito_2
else:
    digito_2 = 0
cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'
# validação do CPF inserido com o calculo
if cpf_usuario == cpf_calculo:
    print(f'{cpf_usuario} é um CPF válido')
else:
    print(f'{cpf_usuario} é um CPF inválido')