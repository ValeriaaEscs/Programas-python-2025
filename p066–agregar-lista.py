# Ejemplificar el como agregar elementos a una lista de numeros

import os; os.system('clear')

nums = [80.3, 12.5, 60.2, 20.4]

print('Agregar elementos a una lista numerica existente')

print(f'La lista es {nums}, tiene {len(nums)} elementos ')

print('\nAgregar elementos al final de la lista usando el metodo append() ')
nums.append(90)
nums.append(100)
print(f'La lista es {nums}, tiene {len(nums)} elementos ')

print('\nInsertar dos numeros en una posicion determinada usando el metodo insert()')
nums.insert(4, 80)

print(f'La lista es {nums}, tiene {len(nums)} elementos ')

print('\nInsertar mas de un elemento a la vez, en una posicion determinada, usando un slice')