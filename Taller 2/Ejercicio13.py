"""
Entradas
examate-->float-->em
tareamate1-->float-->tm1
tareamate2-->float-->tm2
tareamate3-->float-->tm3 
examfisica-->float-->ef 
tareafisi1-->float-->tf1
tareafisi2-->float-->tf2 
examquim-->float-->eq
tareaquimi1-->float-->tq1 
tareaquimi2-->float-->tq2
tareaquimi3-->float-->tq3 

Salidas
promediomate-->float-->pm
promediofisica-->float-->pf 
promedioquimica-->float-->pq
promediototal-->float-->pt 
"""

em = float(input("Digite la nota de examen matemmaticas: "))
tm1 = float(input("Digite la nota de tarea matematicas1: "))
tm2 = float(input("Digite la nota de tarea matematicas2: "))
tm3 = float(input("Digite la nota de tarea matematicas3: "))

pm = 0.90 * em + 0.10 * (tm1 + tm2 + tm3) / 3
print("El promedio de matematicas es: " + str(pm))

ef = float(input("Digite la nota de examen fisica: "))
tf1 = float(input("Digite la nota de tarea fisica1: "))
tf2 = float(input("Digite la nota de tarea fisica2: "))

pf = 0.80 * ef + 0.20 * (tf1 + tf2) / 2
print("El promedio de fisica es: " + str(pf))

eq = float(input("Digite la nota de examen quimica: "))
tq1 = float(input("Digite la nota de tarea quimica 1: "))
tq2 = float(input("Digite la nota de tarea quimica 2: "))
tq3 = float(input("Digite la nota de tarea quimica 3: "))

pq = 0.85 * eq + 0.15 * (tq1 + tq2 + tq3) / 3
print("El promedio de quimica es: " + str(pq))

pt = (pm + pf + pq) / 3

total = pt
print("El promedio de las tres materias es: " + str(total))