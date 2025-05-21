# Ejemplificar el uso de una funcion que recibe 3 parametros numericos y devuelve cual es mayor
import os

def mayor(c1, c2, c3):
    may = 0
    if c1>c2 and c1>c3:
        may = c1
    elif c2>c1 and c2>c3:
        may = c2
    elif c3>c1 and c3>c2:
        may = c3
    return may

os.system('clear')
print('Dame 3 calificaciones y te dire cual es el mayor')
a, b, c = float(input()), float(input()), float(input())
m = mayor(a, b, c)
if m==0 :
    print('Error: no hay un numero mayor')
else:
    print(f'El numeromayor es {m}')