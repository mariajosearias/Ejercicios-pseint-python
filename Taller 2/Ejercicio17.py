"""
Entradas
presupuestoanual-->float-->pa

Salidas
AreaGinecologia-->float-->ag
AreaTraumologia-->float-->at
AreaPediatria-->float-->ap

"""
pa=float(input("Digite presupuesto anual"))

ag= pa*0.40
at= pa*0.30
ap= pa*0.30

print ("Al area de ginecologia le corresponde " +str(ag))
print ("Al area de traumologia le corresponde " +str(at))
print ("Al area de pediatria le corresponde " +str(ap))