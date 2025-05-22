# Crear los conjuntos A, B y C
A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

# Mostrar los conjuntos
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

# Operaciones entre conjuntos
print("\nOperaciones entre conjuntos:")
print("Unión A | B:", A | B)
print("Unión B | C:", B | C)
print("Diferencia A - C:", A - C)
print("Diferencia simétrica B ^ C:", B ^ C)
print("Intersección B & C:", B & C)

# Preguntas booleanas
print("\nResultados de preguntas:")
print("¿A es subconjunto de B?:", A.issubset(B))
print("¿C es subconjunto de A?:", C.issubset(A))
print("¿100 está en A?:", 100 in A)
print("¿60 está en A, B y C?:", 60 in A and 60 in B and 60 in C)
print("¿900 no está en C?:", 900 not in C)
