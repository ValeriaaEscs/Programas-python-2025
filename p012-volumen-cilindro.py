# Calcular el volumen del cilindro

import math

r = float(input('Dar el valor del radio: '))
a = float(input('Dar el valor de la altura: '))


v = math.pi * (r** 2) + a

print(f'El volumen del cilindro es de: {v:,.0f}')