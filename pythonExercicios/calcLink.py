media_de_usuario_online = 500
garantia_de_link = 15 # (%)
velocidade_unitaria = 128 # kbit/s
velocidade_link = (garantia_de_link / 100) * (media_de_usuario_online * velocidade_unitaria)
print(velocidade_link)

'''
media_de_usuario_online = 500
velocidade_link = 3200 # kbit/s
velocidade_unitaria = 128 # kbit/s
unidades_reais = velocidade_link / velocidade_unitaria
notacao = media_de_usuario_online / unidade_reais
'''