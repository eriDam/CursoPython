import sys
if len(sys.argv) == 3:
	filas= int(sys.argv[1])
	columnas = int(sys.argv[2])

	if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
		print("Error - Argumentos incorrectos")
		print("Ejemplo:tabla.py [1-9] [1-9] ")
	else:
		#Aqui empieza la lógica
		for f in range(filas):
			#print para que se ejecute las ve4ces que le pasemos
			print()
			for c in range(columnas):
				print(" * ", end='') #(end='' evita el salto de línea)


else:

	print("Error - Argumentos incorrectos")
	print("Ejemplo:tabla.py [1-9] [1-9] ")
