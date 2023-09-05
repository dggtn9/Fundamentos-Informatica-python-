#Ejercicio 8
"""Leer una medida en metros e imprimir esta medida expresada en centímetros,
pulgadas, pies y yardas. Los factores de conversión son:
· 1 pie = 12 pulgadas
· 1 yarda = 3 pies
· 1 pulgada = 2,54 cm.
· 1 metro = 100 cm."""

medidad_metros=int(input("Inserte medida en metros="))
medida_en_cm=(medidad_metros*100)
medida_en_pulgadas=(medida_en_cm/2.54)
medida_pies=(medida_en_pulgadas/12)
medida_yardas=(medida_pies/3)

print("Medida en cm="+ str(medida_en_cm))
print("Medida en pulgadas="+str(medida_en_pulgadas))
print("Medida en pies="+str(medida_pies))
print("Medida en yardas="+str(medida_yardas))




