"""
Entradas
Consumoenergia-->float-->ce
costo-->float-->c
Salidas
pago-->float-->p

"""

ce=float(input("Digite el numero de consumo de energia electrica en kilovatios "))
c=float(input("Digite el costo en pesos por kilovatio " ))

p=ce*c

print ("El total a pagar de energia electrica es: " +str(p))

