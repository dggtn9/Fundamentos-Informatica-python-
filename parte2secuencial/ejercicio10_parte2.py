#Ejercicio 10
"""Leer un período en segundos e imprimirlo expresado en días, horas,
minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días,
7 horas, 33 minutos y 20 segundos"""

segundos=int(input("Ingresar valor"))
dias=segundos // 86400

print("dias:", dias)

resto = segundos % 86400

horas=resto//3600
print("horas:",horas)

resto= resto % 3600

minutos= resto//60
print("minutos:",minutos)

segundos=resto %60

print("segundos",segundos)











