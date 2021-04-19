Algoritmo Inicio_Area_Triagulo
	Escribir "Ingresa valor lado A"
	Leer ladoa
	Escribir "Ingresa valor lado B"
	Leer ladob
	Escribir "Ingresa valor lado C"
	Leer ladoc
	
	p<-(ladoa+ladob+ladoc)/2
	a<-rc(p*(p-ladoa)*(p-ladob)*(p-ladoc))
	
	Escribir "Escribir el area del triangulo ", a
	
	
FinAlgoritmo
