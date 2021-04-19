"""
Entradas
cantidadgalones-->float-->cg
Salidas
precio-->float-->p

"""

cg=float(input("Digite cantidad de galones en litro"))

p=(50000*cg)/3785

print ("Se le debe cobrar al cliente: " +str(p))