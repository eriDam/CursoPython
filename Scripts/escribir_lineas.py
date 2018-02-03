import sys
'#Compruebo si lalongitud de los argv es >3 la long de la lista,' 
'#el primer argv es el nombre del script' 
if len(sys.argv)==3:
	texto = sys.argv[1] '#el primer argumento es el nombre'
	'#el segundo arg es un nº serán las rep hacemos un cast a int'
	repeticiones = int(sys.argv[2])  
	for r in range(repeticiones):
	print(texto) '#lo que queremos repetir'
else:
	print("Error, introduce 2 argumentos solo")
	print("Ejemplo: escribir_lineas.py 'Texto' 5")