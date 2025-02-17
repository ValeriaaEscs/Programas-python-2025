# Convertir temperaturas de farenheit a centigrados y viserversa

import os;os.system('clear')

print('Convertir temperaturas de farenheit a centigrados y viserversa')
print('De Centigrados a Farenheit ....[1]')
print('De Farenheit a Centigrados ....[2]')
op = int(input('Elige ? '))

if op ==1:
    print('Convirtiendo de Centigrados a Farenheit ....')
    temp = float(input('Grados Centigrados ? '))
    res = ( temp * 9 / 5 ) + 32
    print(f'{temp} grados centigrados, equivale a {res} grados farenheit')

else:
    print('Convirtiendo de Farenheit a Centigrados....')
    temp = float(input('Grados Farenheit ? '))
    res  = ( temp - 32) * 5 / 9
    print(f'{temp} grados farenheit, equivale a {res} grados centigrados')