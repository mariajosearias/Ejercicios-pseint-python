Algoritmo Inicio_Promedio_General
	Escribir 'Ingrese la nota del examen de matematica'
	Leer examate
	Escribir 'Ingrese las notas de las tareas'
	Leer tareamat1,tareamat2,tareamat3
	mate <- 0.90*examate+0.10*(tareamat1+tareamat2+tareamat3)/3
	Escribir 'el promedio de matematica es: ',mate
	Escribir 'Ingrese la nota del examen de fisica: '
	Leer examfisi
	Escribir 'Ingrese las notas de las tareas: '
	Leer tareafisi1,tareafisi2
	fisica <- 0.80*examfisi+0.20*(tareafisi1+tareafisi2)/2
	Escribir 'El promedio de la fisica es: ',fisica
	Escribir 'Ingrese la nota del examen de quimica: '
	Leer examquim
	Escribir 'Ingrese las notas de las tareas: '
	Leer tareaquim1,tareaquim2,tareaquim3
	quimica <- 0.85*examquim+0.15*(tareaquim1+tareaquim2+tareaquim3)/3
	Escribir 'El promedio de la quimica es: ',quimica
	Promedio <- (mate+fisica+quimica)/3
	Escribir 'El promedio de las tres materias es: ',Promedio
FinAlgoritmo
