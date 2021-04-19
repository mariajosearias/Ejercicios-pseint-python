Algoritmo Inicio_Salario_Neto
	Escribir "Digite valor sueldo base"
	Leer sueldoba
	Escribir "Digite el numero de horas trabajadas diarias"
	Leer horasdiarias
	Escribir "Digite los dias trabajados"
	Leer diastrabaja
	
	horastrabajadas<-horasdiarias*diastrabaja
	valorhora<-sueldoba/horastrabajadas
	impuesto<-sueldoba*0.20
	Salarioneto<-sueldoba-impuesto
	
	Escribir "Trabajo ", horastrabajadas, " horas"
	Escribir "El precio de la hora es ", valorhora
	Escribir "El impuesto del 20% es ", impuesto
	Escribir "El salario neto que debe recibir es ", Salarioneto

	
FinAlgoritmo
