"""
Entradas
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->v3
sueldobase-->float-->sb
Salidas
comision-->float-->c
total-->float-->total
"""



v1=float(input("Digite la venta1: "))
v2=float(input("Digite la venta2: "))
v3=float(input("Digite la venta3: "))
sb=float(input("Digite sueldo base: "))


c=(v1+v2+v3)*0.10
total=sb+c

print("La comision es: "+str(c), " sueldo total: "+str(total))


