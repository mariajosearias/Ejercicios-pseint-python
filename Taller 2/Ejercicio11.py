"""
Entradas
numerohijos-->float-->nh
sueldobase-->float-->sb 
horastrabajadas-->float-->ht 
horasextra-->float-->he
Salidas
d-->float-->dia
horas-->float-->h
sueldo-->float-->s   
horasextra2-->float-->he2
horasextra3-->float-->he3
paroforzoso-->float-->pf 
politicahabitacional-->float-->ph 
cajadeahorro-->float-->ca 
deducciones-->float-->d  
asignaciones-->float-->a  
sueldoneto-->float-->sn    
"""

nh=float(input("Digite numero de hijos"))
sb=float(input("Digite sueldo base"))
ht=float(input("Digite horas trabajadas"))
he=float(input("Digite horas extra trabajadas"))

d=(sb/31)
h=(d/8)
s=(h*ht ) 
he2=(he*0.25)
he3=(he2+h)
pf=(sb*0.05)
ph=(sb*0.02)
ca=(sb*0.07)
d=(pf+ph+ca)
a=(250000+(173000*(nh))+180000)

sn=((s+a+he3)-d)

print ("Las deducciones seran" +str(d))
print ("Las asignaciones son" +str(a))
print ("El sueldo neto sera de " +str(sn))
