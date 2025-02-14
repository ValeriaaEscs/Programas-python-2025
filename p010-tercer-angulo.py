# Calcular el tercer angulo, dado dos angulos de un triangulo



a =float(input('Valor del angulo a : '))
b =float(input('Valor del angulo b : '))

#Formula para calcular el tercer angulo
c = 180 - (a + b)

print(f'El tercer angulo es: {c:.0f}')
