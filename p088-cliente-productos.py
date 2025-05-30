# Procesar clientes y sus productos en un diccionario
# Calcular el subtotal de cada cliente en otro diccionario 

import os; os.system('clear')

compras = [
     {'cliente' : 'Carlos', 'producto': 'pinzas', 'cantidad' : 250.55},
    {'cliente' : 'Rocio', 'producto': 'martillo', 'cantidad' : 95.32},
    {'cliente' : 'Pedro', 'producto': 'pinzas', 'cantidad' : 250.55},
]

n = int(input('Cuantas compras mas deseas agregar ? '))
for c in range(1, n+1):
    print(f'\nCompra {n}')
    compra = {
        'cliente' : input('Nombre :'),
        'producto' : input('Producto :'),
        'cantidad' : int(input('Cantidad :')),
        'precio'   : float(input('Precio'))
    }
    compras.append(compra)


clientes = {}
for compra in compras:
    cliente = compra ['cliente']
    if cliente not in clientes:
        clientes[cliente] = {'cantidad': 0, 'subtotal' :0}
    clientes[cliente]['cantidad'] += compra['cantidad']
    clientes[cliente]['subtotal'] += compra['cantidad'] * compra['precio']


    print(f'Clientes : {clientes} - {len(clientes)}')
    for cliente, datos in clientes.items():
        print('Cliente : ', cliente )
        print(f'Cantidad : {datos['cantidad'] : .2f} ')
        print(f'Subtotal : {datos['subtotal'] : .2f} ')
        print()