"""
entradas
hombres-->float-->h
mujeres-->float-->m
salidas
total-->float-->t
porcentajehombres-->float-->ph
porcentajemujeres-->float-->pm
"""
h=float(input("Digite la cantidad de hombres "))
m=float(input("Digite la cantidad de mujeres "))
t=(h+m)
ph=((h*100)/t)
pm=((m*100)/t)

print ("El total de personas en el aula es de: "+str(t) )
print ("El porcentaje de hombres es de " +str(ph), "%")
print ("El porcentaje de mujeres es de " +str(pm), "%")