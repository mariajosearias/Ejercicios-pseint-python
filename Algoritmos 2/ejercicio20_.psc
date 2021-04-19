Algoritmo Inicio_Precio_Computadores
	Escribir "Precio Computadores"
	Leer Preciocompu
	Escribir   "Digite la razon Numerica de la tasa"
	Leer Porcentasa
	
	Preciocuota<-((Porcentasa*Preciocompu)/1-(1+Porcentasa)^12)
	
	
	Escribir "El precio de los intereses mensualmente sera de:", Preciocuota, "%"
	
FinAlgoritmo
