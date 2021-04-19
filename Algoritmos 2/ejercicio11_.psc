Algoritmo Inicio_sueldo
	Escribir  "Ingrese su nombre"
	Leer nombre
	Escribir "Digite numero de hijos"
	Leer hijos
	Escribir "Ingrese sueldo base"
	Leer sueldob
	Escribir "Ingrese horas trabajadas"
	Leer horastrab
	Escribir "Ingrese horas extras realizadas"
	Leer horasextr
	
	dia<-(sueldob/31)
	horas<-(dia/8)
	sueldo<-(horas*horastrab)
	horasextra<-(horasextr*0.25)
	horaextraf<-(horasextra+horas)
	paroforzoso<-(sueldob*0.05)
	politicahabitacional<-(sueldob*0.02)
	cajadeahorro<-(sueldob*0.07)
	deducciones<-(paroforzoso+politicahabitacional+cajadeahorro)
	asignaciones<-(250000+(173000*(hijos))+180000)
	sueldoneto<-((sueldo+asignaciones+horaextraf)-deducciones)
	
	Escribir "Las deducciones son: " deducciones
	Escribir "Las asignaciones son: " asignaciones
	Escribir "El sueldo neto sera de: " sueldoneto
	
	
FinAlgoritmo
