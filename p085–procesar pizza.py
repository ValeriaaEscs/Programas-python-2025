# Procesar el pedido de una pizza con diferentes ingredientes 

import os; os.system('clear')

ingredientes = {
    'T' : 1.50,
    'P' : 3.50,
    'C' : 3.74,
    'A' : 0.40
}

base = 15
subtotal = 0 
total = 0
descuento = 0

pedido = input('Ingredientes (T)omate, (P)eperoni, (C)hampiñones, (A)guacate ').upper()

for ingrediente in pedido:
    if ingrediente in ingredientes:
        subtotal = subtotal + ingredientes[ingrediente]

subtotal = subtotal + base
total = subtotal
if subtotal >= 20:
    descuento = subtotal * 0.05
    total = subtotal - descuento
    print(f'Los ingredientes que elegiste fueron : {pedido}')
    print(f'El subtotal a pagar sin descuento es : {subtotal}')
    print(f'El importe del descuento es     : {descuento}')
    print(f'\nTotal a pagar : {total}')