# Dar 4 digitos para tener el numero  suerte con el año cuando nacio

año = int(input('Ingrese su año de nacimiento (4 dígitos): '))

# Extraer los dígitos individuales
d1 = año // 1000
d2 = (año // 100) % 10
d3 = (año // 10) % 10
d4 = año % 10

# Calcular la suma de los dígitos
suma_digitos = d1 + d2 + d3 + d4

# Mostrar resultados
print("Los dígitos individuales del año son:", d1, d2, d3, d4)
print("La suma de los dígitos es:", suma_digitos)
