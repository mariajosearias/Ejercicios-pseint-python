"""
Entradas
bolivaresprestados-->float-->bp
razon-->float-->r
salidas
interes-->float-->i
"""
bp=float(input("Digite la cantidad de bolivares prestados "))
r=float(input("Digite la razon numerica del interes "))

i=(bp*4*r)/100

print("el interes es de " +str(i))