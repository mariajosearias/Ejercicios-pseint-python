Algoritmo Inicio_Monto_Factura
	Definir CE, COSTO, PAGO Como Real
	Escribir "Ingrese el numero de consumo de Energia electrica en kilovatio"
	Leer CE
	Escribir "Ingrese el costo en pesos por kilovatio"
	Leer COSTO
	
	PAGO<-CE*COSTO
	Escribir "Total a pagar en pesos: ", PAGO
	
FinAlgoritmo
