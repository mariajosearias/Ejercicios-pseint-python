"""
Entradas
lotesnaranja-->float-->ln
precio-->float-->p
venta-->float-->v
Salidas
porcentaje-->float-->pr
"""
ln=float(input("Ingrese la cantidad de lotes de naranja "))
p=float(input("Ingrese precio por docenas de narnaja "))
v=float(input("Ingrese el valor venta: "))

nd=(ln/12)
costo=(p*nd)
ganancia=(v-costo)
p=((ganancia*100)/costo)

print("El porcentaje de ganancias es de :" +str(p))