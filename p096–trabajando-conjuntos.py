# Muestra las operaciones basicas sobre conjutos 

import os ; os.system('clear')

muns = {'Zacatecas','Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('Ejemplificando las operaciones basicas sobre conjuntos')

print(f'El conjunto : {muns} - {len(muns)}')

print('\nLista de municipios usando un ciclo')

print('\nZacatecas esta en el conjunto d eun municipio: ', 'Zacatecas' in muns)

print('Agregar un elemento al conjunto')
muns.add('Teul')
print(f'El conjunto : {muns} - {len(muns)}')

print('\nAgregar varios elementos a un conjunto')
otros = {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
muns.update(otros)
print(f'El conjunto : {muns} - {len(muns)}')

print('\nEliminar  elementos de un  conjunto')
muns.remove('Zacatecas')
muns.discard('Ojocaliente')
muns.pop()
print(f'El conjunto : {muns} - {len(muns)}')

print('\nEliminar todos los elementos del conjunto')
muns.clear()
print(f'El conjunto : {muns} - {len(muns)}')