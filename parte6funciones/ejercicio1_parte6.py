numero=int(input("Ingrese numero,ingrese -1 para terminar="))

cantidad_de_numeros_ingresados=0

while numero!=-1:
    cantidad_de_numeros_ingresados = cantidad_de_numeros_ingresados+1
    if cantidad_de_numeros_ingresados==1:
        primernumero=numero
    ultimo_numero=numero
    numero=int(input("Ingrese numero,ingrese -1 para terminar="))
print(" El primer numero es igual a=",primernumero)
print("El ultimo numero es=",ultimo_numero)
