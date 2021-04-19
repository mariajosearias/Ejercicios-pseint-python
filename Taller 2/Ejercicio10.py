"""
Entradas
chelin-->float-->c
dragma-->float-->d
peseta1-->float-->p1
peseta2-->float-->p2
Salidas
chelapese-->float-->ch
dracaff-->float-->dr
pesetaddolar-->float-->psd
pesetalira-->float-->psl
"""
c=float(input("Digite la cantidad de chelines austricos que desea convertir a pesetas: "))
d=float(input("Digite la cantidad de dracmas griegos que desea convertir a francos griegos: "))
p1=float(input("Digite la cantidad de pesetas que desea convertir a dolares: "))
p2=float(input("Digite la cantidad de pesetas que desea convertir a liras italianas: "))

ch=(c*9.56871)
dr=((d*886.07)/20.110)
psd=(p1*0.00000816333)
psl=(p2*92.89)

print (str(c), "chelines son = " +str(ch), "pesetas ")
print (str(d), "dragmas son = " +str(dr), "francos italianos, ")
print (str(p1), "pesetas son = " +str(psd), "dolares ")
print (str(p2), "pesetas son = " +str(psl), "liras italianas ")
