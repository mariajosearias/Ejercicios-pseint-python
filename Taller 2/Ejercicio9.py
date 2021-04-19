"""
Entradas
salariobase-->float-->sb
horasdiarias-->float-->hd
diastrabajados-->float-->dt
salida
horastrabajadas-->float-->ht
valorhora-->float-->vh
impuesto-->float-->i
salarioneto-->float-->sn
"""
sb=float(input("Digite valor sueldo base"))
hd=float(input("Digite el numero de horas trabajadas diarias"))
dt=float(input("Digite los dias trabajados"))

ht=hd*dt
vh=sb/ht
i=sb*0.20
sn=sb-i

print ("Se trabajo " +str(ht), "horas.")
print ("El valor por hora es de: "+str(vh))
print ("el impuesto del 20% es: "+str(i))
print ("El salario que debe recibir es: " +str(sn))