# Llevar el control de la inscripcion a un evento academico de la Universidad Patito; tipo de usuario, paquete y la cantidad

import os
os.system('clear')
total_ventas = 0

while(True):
 print('Tipo de usuario')
 print('Usuario: Alumno (100) ....[1]')
 print('Usuario: Trabajador (200) ....[2]')
 print('Usuario: Docente (500)....[3]')
 Usuario = int(input('Elige ? '))

 if Usuario == 1 :
   precio_usuario = 100
   descuento = 0.20
 elif Usuario == 2 :
   precio_usuario = 200
   descuento = 0.10
 elif Usuario == 3 :
   precio_usuario = 500
   descuento = 0.05
 else:
   print('Tipo de usuario no válido, intente de nuevo por favor.')

 print('Tipo de paquete')
 print('Paquete: Solo conferencias (600) ....[1]')
 print('Paquete: Eventos sociales (800) ....[2]')
 print('Paquete: Kit de acceso (900)....[3]')
 Paquete = int(input('Elige ? '))

 if Paquete == 1 :
   precio_paquete = 600
 elif Paquete == 2 :
   precio_paquete = 800
 elif Paquete == 3:
   precio_paquete = 900
 else:
    print('Tipo de paquete no válido, intente de nuevo por favor.')

 cantidad = int(input('Ingrese la cantidad de inscripciones:  '))

 subtotal = (precio_usuario + precio_paquete) * cantidad

 if subtotal > 5000:
   descuento_a = subtotal * descuento
 else:
   descuento_a = 0

 total_pagar = subtotal - descuento_a
 total_ventas += total_pagar

 # Resumen de la venta
 print('\nResemne de la venta ')
 print('Tipo de usuario:', Usuario,'($', precio_usuario, ')')
 print('Tipo de usuario:', Paquete,'($', precio_paquete, ')')
 print('Cantidad:', cantidad)
 print('Subtotal: $', subtotal)
 print('Descuento Aplicado: $', descuento_a)
 print('Total a pagar: $', total_pagar)

 if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nTotal de ventas del día : $', total_ventas)
print('\nProceso Terminado, gracias por inscribirte :)')