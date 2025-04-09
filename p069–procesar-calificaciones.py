# Procesar n calificaciones introducidas por un usuario

import os ; os.system('clear')

nums = []
mp = []
n = suma = prom = 0

print('Procesamiento de calificaciones ...')

while n!=999:
    n = float(input('Calificaciones [1-10] >'))
    if n>0 and n<=10:
        nums.append(n)
    else:
        print('>(')

nums.sort()
print(f'\n < fin > {nums} - {len(nums)}')

suma = sum(nums)
prom = suma / len(nums)

for n in nums :
    if n > prom:
        mp.append(n)

print('\nEstadisticas')
print(f'La suma es          : {suma}')
print(f'El promedio         : {prom}')
print(f'Mayores al promedio : {mp} - {len(mp)}')
