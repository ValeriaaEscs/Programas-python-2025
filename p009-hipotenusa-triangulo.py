# Calcular la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados

import math

a = float(input('Valor del cateto a: '))
b = float(input('Valor del cateto b: '))

#Formula de la hipotenusa
c = math.sqrt(a**2 + b**2)

print(f'La hipotenusa es: {c:.0f}')