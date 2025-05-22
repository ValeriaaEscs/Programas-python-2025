empleados = []

while True:
    print("\n--- Captura de Empleado ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (h/m): ").lower()
    pasatiempos = input("Pasatiempos (separados por comas): ").split(",")
    sueldo = float(input("Sueldo: $"))
    
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "pasatiempos": [p.strip() for p in pasatiempos],
        "sueldo": sueldo
    }
    
    empleados.append(empleado)
    
    continuar = input("¿Deseas capturar otro empleado? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar datos como se guardan
print("\n--- Lista de Diccionarios ---")
for e in empleados:
    print(e)

# Mostrar datos en formato tabular
print("\n--- Datos en Formato Tabular ---")
print(f"{'Nombre':<15}{'Edad':<6}{'Sexo':<6}{'Pasatiempos':<30}{'Sueldo':<10}")
for e in empleados:
    print(f"{e['nombre']:<15}{e['edad']:<6}{e['sexo']:<6}{', '.join(e['pasatiempos']):<30}${e['sueldo']:<.2f}")

# Resumen
total_empleados = len(empleados)
total_hombres = sum(1 for e in empleados if e["sexo"] == 'h')
total_mujeres = sum(1 for e in empleados if e["sexo"] == 'm')

# Pasatiempos
pasatiempo_contador = {}
for e in empleados:
    for p in e["pasatiempos"]:
        pasatiempo_contador[p] = pasatiempo_contador.get(p, 0) + 1

suma_edad = sum(e["edad"] for e in empleados)
promedio_edad = suma_edad / total_empleados if total_empleados > 0 else 0

suma_sueldo = sum(e["sueldo"] for e in empleados)
promedio_sueldo = suma_sueldo / total_empleados if total_empleados > 0 else 0

mayor_edad = max(empleados, key=lambda e: e["edad"])
menor_edad = min(empleados, key=lambda e: e["edad"])

# Mostrar resumen
print("\n--- Resumen ---")
print(f"Total de empleados: {total_empleados}")
print(f"Hombres: {total_hombres}")
print(f"Mujeres: {total_mujeres}")
print("\nEmpleados por pasatiempo:")
for p, c in pasatiempo_contador.items():
    print(f"- {p}: {c}")
print(f"\nSuma de edades: {suma_edad}")
print(f"Promedio de edad: {promedio_edad:.2f}")
print(f"Suma de sueldos: ${suma_sueldo:.2f}")
print(f"Promedio de sueldo: ${promedio_sueldo:.2f}")
print(f"Empleado de mayor edad: {mayor_edad['nombre']} ({mayor_edad['edad']} años)")
print(f"Empleado de menor edad: {menor_edad['nombre']} ({menor_edad['edad']} años)")
