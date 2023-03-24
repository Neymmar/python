'''
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
'''
import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
