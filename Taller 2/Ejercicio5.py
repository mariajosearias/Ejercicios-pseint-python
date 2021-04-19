"""
Entradas
nota1-->float-->n1
nota2-->float-->n2
nota3-->float-->n3
examenfinal-->float-->ef
trabajofina-->float-->tf
Salidas
promedio-->float-->p
promedioparcial-->float-->pp
promedioexamenfinal-->float-->pef
promediotrabajofinal-->float-->ptf
calificacionfinal-->float-->cf
"""

n1=float(input("Ingrese la calificacion #1 "))
n2=float(input("Ingrese la calificacion #2 "))
n3=float(input("Ingrese la calificacion #3 "))
ef=float(input("Ingrese la calificacion del examen final"))
tf=float(input("Ingrese la calificacion del trabajo final"))

p=(n1+n2+n3)/3
pp=p*0.55
pef=ef*0.30
ptf=tf*0.15
cf=pp+pef+ptf

print ("la calificacion final sera " +str(cf))