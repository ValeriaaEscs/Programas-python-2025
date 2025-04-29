# Lista para almacenar nombres de ciudades
ciudades = []


while True:
    ciudad = input("Ingresa el nombre de una ciudad (o $ para terminar): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)


print(f"\nCantidad de ciudades: {len(ciudades)}")
print("Lista de ciudades ingresadas:")
print(ciudades)


ciudades.sort(reverse=True)
print("\nLista ordenada en orden descendente:")
print(ciudades)


vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
consonantes = []
for ciudad in ciudades:
    if not ciudad.startswith(vocales):
        consonantes.append(ciudad)

print(f"\nCantidad de ciudades que inician con consonante: {len(consonantes)}")
print("Ciudades que inician con consonante:")
for c in consonantes:
    print(c)