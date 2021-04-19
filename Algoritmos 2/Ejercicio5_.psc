Proceso Inicio_Calificaciones
	Escribir "ingrese primera calificacion"
	Leer cal1
	Escribir "ingrese segunda calificacion"
	Leer cal2
	Escribir "ingrese tercera calificacion"
	Leer cal3
	
	Escribir "ingrese calificacion del examen final"
	Leer ef
	
	Escribir "ingrese calificacion del trabajo final"
	Leer tf
	
	promedio= (cal1+cal2+cal3)/3
	
	pparcial= promedio*0.55
	pef= ef*0.30
	ptf= tf*0.15
	
	calf= pparcial+pef+ptf
	
	Imprimir "su calificacion final es:  ", calf
FinProceso
