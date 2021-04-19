"""
Entradas
inversion-->float-->i
tiempo-->float-->t
Salidas
ganancia-->float-->g
"""

i=float(input("Digite el valor de la inversion"))
t=float(input("Digite el tiempo en meses"))

g=(i*(0.02*t))

print("La ganancia sera de  " +str(g))