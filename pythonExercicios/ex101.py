def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano 
    if idade <= 16:
        return f'Com {idade} anos: Seu voto é opcional !'
    elif idade > 65 or  16 <= idade < 18:
        return f'Com {idade} anos: Não necessita votar !'
    else:
        return f'Com {idade} anos: Voto obrigatório !'


nasc = ano = int(input('Em que ano você nasceu ? '))
print(voto(nasc))
