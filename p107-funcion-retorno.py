# Ejemplificar el uso de valores de retornos en la funcion 
import os

def suma(n1,n2):
    s = n1 + n2 
    return s

os.system('clear')
print('\nInvocando a una funcion como dos parametrtos, y recibiendo el valor de retorno')

res = suma(10,20) # guardamos el resultado en un variable 
print(f'\nEl resultado de la suma es {res}')

print('\nDame dos numeros enteros y te calculare la suma: ')
a, b = int(input()), int(input())
print(f'\nLa suma d elos numeros que me diste es {suma(a, b):,.2f}')
