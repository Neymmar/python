import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O seno, cosseno e tangente do ângulo de {ang}º são respectivante: sen {seno:.2f}º, cos {coss:.2f}º, tan {tang:.2f}º')