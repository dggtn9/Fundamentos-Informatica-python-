"""Ingresar un número N y validar que sea positivo. Luego:
a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b. Informar la suma de esos números impares.
Ejemplo:
· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
· Si se ingresa -5, se debe pedir otro número."""

N= int(input("Ingrese un número positivo: "))
if N>=1:
          print("su numero es positivo")
else:
          print("Por favor, ingrese un número positivo.")
# Mostrar los primeros números impares y calcular la suma
suma_impares = 0
for i in range(1, N + 1, 2):
    print(i, end=" ")
    suma_impares += i

print("\nLa suma de los números impares es:", suma_impares)
print("Este código primero solicita al usuario que ingrese un número positivo y valida si es positivo o no. Si no es positivo, solicitará al usuario que lo ingrese nuevamente. Luego, utiliza un bucle for para generar los números impares y calcular su suma, mostrando los números impares en el proceso. Finalmente, muestra la suma de los números impares.")










