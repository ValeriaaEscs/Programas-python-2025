# Crear los conjuntos A y B
A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print("Conjunto A:", A)
print("Conjunto B:", B)

# Unión de los conjuntos
union = A | B
print("Unión A | B:", union)

# Intersección de los conjuntos
interseccion = A & B
print("Intersección A & B:", interseccion)

# Diferencia A - B
diferencia = A - B
print("Diferencia A - B:", diferencia)

# Diferencia simétrica A ^ B
dif_simetrica = A ^ B
print("Diferencia simétrica A ^ B:", dif_simetrica)

# Subconjunto: ¿{"Pablo", "Mateo"} es subconjunto de B?
subconjunto = {"Pablo", "Mateo"}
print("¿Pablo y Mateo ⊆ B?:", subconjunto <= B)

# Superconjunto: ¿A es superconjunto de {"Reynaldo", "Angelica"}?
otros = {"Reynaldo", "Angelica"}
print("¿A ⊇ {'Reynaldo', 'Angelica'}?:", A >= otros)

# ¿Pedro está en A?
print("¿Pedro ∈ A?:", "Pedro" in A)

# ¿Lilia no está en B?
print("¿Lilia ∉ B?:", "Lilia" not in B)