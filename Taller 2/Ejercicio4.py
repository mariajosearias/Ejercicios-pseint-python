"""
Entradas
valorcompra-->float-->vc
Salidas
descuentos-->float-->d
preciofinal-->float-->pf
"""
vc=float(input("Digite el valor de la compra " ))

d=(vc*0.15)
pf=(vc-d)

print("El valor total a pagar es de " +str(pf), "El descuento total  es" +str(d))
