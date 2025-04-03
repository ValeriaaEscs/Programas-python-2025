# Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

import math

n = int(input(' Cuantos terminos ? '))

suma = 0
resultado = ''

for i in range(1, n + 1):
    termino = 1  / math.factorial(i)
    suma += termino
    
    if i == 1:
        resultado += '1'
    else: 
        resultado += f' + 1/{i}!'

print(f'Salida: {resultado}, suma: {suma}')
print('\nProseco Terminado :)')