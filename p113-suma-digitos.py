# Sumar los digitos individuales de un numero entero

import os 

def sumadigitos(n):
    s = 0
    while n != 0:
        dig = n % 10
        s = s + dig 
        #print(n, dig)
        n = n // 10
    return s

os.system('clear')
n = int(input('Dame un numero entero ? '))
s = sumadigitos(n)
print(f'\n La suma de los digitos individuales del numero es {s}')