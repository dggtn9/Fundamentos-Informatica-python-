#Ejercicio 12
"""Escribir un programa para convertir un número binario de 4 cifras en un
número decimal. El número binario se ingresa como un solo número
entero de cuatro dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente.
Este exponente se obtiene de la posición que ocupa el dígito
dentro del número, comenzando desde la derecha con la posición 0. Todos
estos resultados se suman para obtener el valor final. Ejemplo: Convertir
1011 a decimal:
13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11"""


valor=int(input("Ingrese numero binario="))
bit_4=(valor//1000)
print(bit_4)
resto=(valor%1000)
bit_3=(resto//100)
print(bit_3)
resto=(resto%100)
bit_2=(resto//10)
print(bit_2)
bit_1=(resto%10)
print(bit_1)

resultado=((bit_4*8)+(bit_3*4)+(bit_2*2)+(bit_1))


print("resultado en numero decimal",resultado)
          
