# Calcula el factorial de un numero 
# 5 = 5 x 4 x 3 x 2 x 1
import os

def factorial(n):
    f = 1
    for n in range(1, n+1):
        f = f * n
        return f

os.system('clear')
print('\nDame un numero y te regreso el factorial ')
n = int(input('Numero ? '))
f = factorial(n)
print(f'\nEl factorial de {n} es {f}')