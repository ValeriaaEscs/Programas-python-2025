# Solicitar los tres números al usuario
print("Determinar el número mayor entre tres valores.")
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))


mayor = a 

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c


print(f"El número mayor es: {mayor}")