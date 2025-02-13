# Uso de las funciones trigonometricas en python
import math
print('Calculo de las funciones trigonometricas')
angulo = float(input('Dame un angulo en radianes? '))

seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)
salida=('Resumen de funciones\n'
f'El seno : {seno}\n'
f'El coseno  : {coseno}\n'
f'La tangente : {tangente}\n'
f'El angulo {angulo} en radianes, equivale a {grados} grados\n')

print(salida)