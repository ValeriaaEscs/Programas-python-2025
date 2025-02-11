# Calcula la paga total de un trabajador

print('Calculando la paga de un trabajador')

print('Nombre    :')
nombre = input()
print('Horas trabajadas  :')
horas = int(input())
print('Paga por hora    :')
paga = float(input())

tasa = 0.03

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print('Resumen de pagos:\n')
print(f'(El trabajador {nombre},trabajo {horas},con una paga de {paga} pesos por hora, impuestos de {tasa})')
print(f'Paga bruta {pagabruta:,.2f}')
print(f'Impuessto {impuesto:,.2f}')
print(f'Paga neta {paganeta:,.2f}')
