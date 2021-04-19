"""
Entradas
preciocompu-->float-->pc
porcentajetasa-->float-->pt
Salidas
preciocuota-->float-->pc
"""

pc=float(input("Inserte precio del computador "))
pt=float(input("Digite la razon numerica de la tasa "))

pc=((pt*pc)/1-(1+pt)*12)

print ("El precio de los intereses mensualmente sera de: " +str(pc))