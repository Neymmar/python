print('=+' * 20)
print('LISTA DE TIMES DO BRASILEIRÃO 2023')
print('=+' * 20)
times = 'América Mineiro', 'Athletico Paranaense', 'Fluminense', 'Fortaleza',  'Palmeiras', 'Vasco da Gama', 'Internacional', 'Bragantino', 'Flamengo', 'São Paulo', 'Botafogo', 'Goiás', 'Cruzeiro', 'Grêmio', 'Corinthians', 'Cuiabá', 'Galo', 'Santos', 'Bahia', 'Coritiba'
print(f'Os cincos primeiros são: {times[0:5]}')
print(f'Os cincos últimos são: {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
print(f'O Galo está na {times.index("Galo")+1}ª posição')