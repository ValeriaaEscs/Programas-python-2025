# Acceder a los elementos de una lista

import os; os.system('clear')

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('Acceder a los elementos de una lista\n')

print(f'La lista completa es : {len(nums)} elementos')
print(f'Primer elemento : {nums[0]}, Ultimo elemento: {nums[8]}')
print(f'Primero elemento: {nums[-9]}, Ultimo elemento: {nums[-1]} \n')
print(f'Elementos del 2 : 6 : {nums[2:6]}')
print(f'Los primeros 3 : {nums[:3]} \n')
print(f'Los últimos 3 : {nums[6:]} \n')

