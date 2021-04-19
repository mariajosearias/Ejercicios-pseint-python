"""
Entradas
productos-->float-->p
precio-->float-->pr
descuento-->float-->d
Salidas
preciofinal-->float-->pf1
preciofinal2-->float-->pf2

"""

p=str(input("¿Cual es el producto?"))
pr=float(input("Digite el precio del producto"))
d=float(input("Digite el descuento"))

pf1=(pr*d)/100
pf2=(pr-pf1)


print ("El precio final con descuento sera de $" +str(pf2))

