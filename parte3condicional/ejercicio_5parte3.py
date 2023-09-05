"""Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $500, más $3,20 por página con encuadernación
rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación
que incrementa el costo en otros $336. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas."""

nropaginas=int(input("Ingrese numero de paginas"))
costoinicial=500
costosiesmayora300=200
costosiesmayora600=336
costoxpaginasiesmenoroiguala300=3.20
costomas300=(nropaginas+costosiesmayora300+costoinicial)
costo600=(nropaginas+costosiesmayora600+costoinicial)
costoigualomenos300=(nropaginas*costoxpaginasiesmenoroiguala300)+costoinicial
paginasmayoresa600=nropaginas+costoinicial

if nropaginas<=300:
    
    print("costo=",costoigualomenos300)
    print("fin")

elif nropaginas>300:
    print("costo=",costomas300)
    print("fin")

elif nropaginas > 600:
    
    print("costo",costo600)
    print("fin")
