"""
Entradas
metros-->float-->m
Salidas
pulgadas-->float-->In
pies-->float-->ft
"""

m=float(input("Digite la cantidad de metros "))
In=(m*39.27)
ft=(In)/12

print ("La medida en pulgadas sera de " +str(In))
print ("La medida en pies sera de " +str(ft))
