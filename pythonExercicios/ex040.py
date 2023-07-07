nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Sua media foi {media} e você foi aprovado')
elif media < 7 and media >= 5:
    print(f'Sua media foi {media} e você está de recuperação')
else:
    print(f'Sua media foi {media} e você foi reprovado')
