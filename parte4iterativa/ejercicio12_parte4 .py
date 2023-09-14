"""La sucesión de Fibonacci es una sucesión de números enteros donde cada término
se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1.
Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e
imprima los N primeros términos de esta sucesión, como así también la suma de
los mismos"""

# Pedir al usuario la cantidad de términos que desea generar
n = int(input("Ingrese la cantidad de términos de la secuencia de Fibonacci que desea generar: "))

# Inicializar los dos primeros términos
a, b = 0, 1

# Calcular y mostrar los N primeros términos
print(a)
print(b)
for i in range(0,n - 2):
    f = a + b
    a = b
    b = f


# Calcular la suma de los términos



# Imprimir la secuencia de Fibonacci y la suma
print(f)

