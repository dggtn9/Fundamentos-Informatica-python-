"""Una remisería requiere un programa que calcule el precio de un viaje a partir de
la cantidad de kilómetros que desea recorrer el usuario. Para eso cuenta con la
siguiente tarifa:
· Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no
alcanza este mínimo.
· Si recorre entre 0 y 10 km: $30 por km
· Si recorre 10 km o más: $20 por km"""

km=int(input("Ingrese los km de su viaje"))
costo_minimo=250
if km>10:
    preciokm=20
else:
    preciokm=30

costo=preciokm*km

if costo<costo_minimo:
    costo=costo_minimo

print("su viaje cuesta=",costo)









