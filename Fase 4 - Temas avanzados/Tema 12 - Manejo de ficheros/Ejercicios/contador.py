from io import open
import sys

fichero = open("contador.txt", "a+") #abrir en modo append con acceso de lectura, de esta orma si no existe lo va a crear
fichero.seek(0) #ponemos el untero al principio
contenido = fichero.readline() #leemos la primera linea

if len(contenido) == 0: # si es cero es que no hay nada
    contenido = "0" 
    fichero.write(contenido) # escribimos el cero en el fichero

fichero.close() #lo cerramos

# Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido) 

    # En función de lo que el usuario quiera...
    if len(sys.argv) == 2: #como mínimo tendrá 2 args; el nombre del fichero y lo que le pasamos
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)

    # Finalmente volvemos a escribir los cambios en el fichero
    fichero = open("contador.txt", "w")
    fichero.write( str(contador) )
    fichero.close()

except:
    print("Error: Fichero corrupto.")