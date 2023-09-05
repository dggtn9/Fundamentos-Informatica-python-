
#Ejercicio 2
print("12 * 4 + 4 * 5=" + str(12 * 4 + 4 * 5))
print("10 / 3="+str(10 / 3))
print("10 // 3="+str(10//3))
print("12 % 5="+str(12 % 5))

#ejercico3
"""Desarrollar un programa que permita ingresar dos números enteros A y
B a través del teclado. Imprimir su suma y su diferencia."""

a=int(input("Ingrese numero"))
b=int(input("Ingrese numero"))

print("Resultado de la resta=" + str(a-b))
print("Resultado de la suma=" + str(a+b))

#ejercico4
"""Calcular el promedio de las notas que obtiene un alumno al rendir los dos
parciales. """

parcial1=int(input("Ingrese nota del parcial 1="))
parcial2=int(input("Ingrese nota del parcial 2="))

print("promedio="+str((parcial1+parcial2)/2))

#ejercicio 5
"""Escribir un programa que permita ingresar la edad de una persona en
años y la convierta a días, imprimiendo el resultado. Considerar que todos
los años tienen 365 días. """

edad=int(input("Ingrese su edad"))
print("edad en dias="+str(edad*365))

#ejercicio 5
"""Tres personas invierten dinero para fundar una empresa (no necesariamente
en partes iguales). Calcular qué porcentaje invirtió cada una. """
inversion1=int(input("Inversion 1="))
inversion2=int(input("Inversion 2="))
inversion3=int(input("Inversion 3="))

total_invertido=(inversion1+inversion2+inversion3)
print("porcentaje_inversion1="+str((inversion1*100)/total_invertido))
print("porcentaje_inversion2="+str((inversion2*100)/total_invertido))
print("porcentaje_inversion3="+str((inversion3*100)/total_invertido))
                          
                    
