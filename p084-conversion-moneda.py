# Conversion de diferentes monedas a peso mexicano

import os; os.system('clear')

conv = {
    'USD' : 20.50,
    'EUR' : 22.30,
    'GBP' : 25.80,
    'JPY' : 0.19,
    'CAD' : 16.20
}

print('Conversion de diferentes monedas a peso mexicano ')
for m in conv.keys():
    print(m)

while True:
    mon = input('Moneda a convertir ? ').upper()
    if mon in conv:
        break

cant = float(input('Ingresa la cantidad a convertir ? '))

res = cant * conv[mon]

print(f'{cant} {mon}  son {res:,.2f} MXN')
