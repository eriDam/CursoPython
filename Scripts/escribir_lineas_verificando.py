import sys
texto = sys.argv[1] #el primer argumento es el nombre
repeticiones = int(sys.argv[2])   #el segundo arg es un nº serán las rep hacemos un cast a int
for r in range(repeticiones):
	print(texto) #lo que queremos repetir