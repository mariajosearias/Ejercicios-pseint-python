"""
Entradas
ladoa-->float-->la
ladob-->float-->lb
ladoc-->float-->lc
Salidas
perimetro-->float-->p
area-->float-->a
"""

la=float(input("Ingrese lado a "))
lb=float(input("Ingrese lado b "))
lc=float(input("Ingrese lado c "))

p=(la+lb+lc)/2
a=(p*(p-la)*(p-lb)*(p-lc))**(1/2)

print("El area total sera de " +str(a))
