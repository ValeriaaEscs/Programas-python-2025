# Ejempleficar la remocion de elementos de una lista de numeros

import os ; os.system('clear')

nums = [ 1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print(' Eliminar elementos de una lista \n ')

print(f'La lista {nums} , tiene {len(nums)} elementos ')

print('\nRemover la primer ocurrencia de un elemento, usuando el metodo remove() ')
nums.remove(99)
print(f'La lista {nums} , tiene {len(nums)} elementos ')

print('\nRemover un elemento en una posicion determinada y guardarlo, usando el metodo pop(x)')
num = nums.pop(8)
print(f'La lista {nums} , tiene {len(nums)} elementos , elemneto removido {num}')

print('\nRemover el ultimo elementos de la lista y guardarlo, usuando el metodo pop()')
num = nums.pop()
print(f'La lista {nums} , tiene {len(nums)} elementos , elemneto removido {num}')

print('\nRemover un rango de valores en una lista, usando el metodo del [:]')
del nums [2:5]
print(f'La lista {nums} , tiene {len(nums)} elementos ')

print('\nEliminar todos los elementos de la lista, usando del metodo clear() ')
nums.clear()
print(f'La lista {nums}, tiene {len(nums)} elementos ')