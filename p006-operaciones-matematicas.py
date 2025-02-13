# Operaciones matematicas

import os;os.system('clear')

#date de prueba 
#x = 10.5
#y = 2.5

x = float(input('Valor de x ? '))
y = float(input('Valor de y ? '))

suma = x+y
resta = x-y
mult = x*y
div = x/y
res = x % y
exp = x ** y
dive = x // y
print(f'suma {suma}\nresta {resta}\nmultiplicacion {mult}\ndivision {div}')
print(f'residuo {res}\nexponenciacion {exp}\ndivision entera {dive}')