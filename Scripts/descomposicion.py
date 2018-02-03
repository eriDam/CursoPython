#importamos sys que contiene la lista de argumentos
import sys
#comprobamos
if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 0 or numero > 9999:
		print("Error - Número incorrecto")
		print("Ejemplo:decomposicion.py [0-9999]")
	else:
		"""Lógica 
		 	cuantas veces hay que recorrer el nº, bucle que 
		 	entre 4 veces(miles, centenas, decenas y unds. 
		 	Hay q transformar el nº a una 
		 	cadena para ver la longitud y 
		 	así determinar las veces q entra"""
		cadena = str(numero)
		longitud = len(cadena)

		for i in range(longitud):
			#tenemos que transformar a int antes de pasarle al format d numeros una cadena 
			#print( "{:04d}".format(int(cadena[i])))
			"""para que salga con este foramto, 
				debemos pasarle la longitud de la cadena -1 - el indice
				0007
  				0040
 				0600
  				3000
  				Por que la longitud hará referencia al largo de la cadena, 
  				por eso restamos 1, así la recorremos del revés"""
			#print( "{:04d}".format(int(cadena[longitud-1-i])))
			"""Tenemos que posicionar los numeros en la unidad que le corresonde
			con matemáticas lo  vamos a multiplicar x las unidades, decenas, centenas
			y miles, después lo vamos a elevar a 0, cualquier nº elevado a 0 vale 1"""
			
			print( "{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i))
			#resultado
			"""
				0007
				0040
				0600
				3000
			"""
else:
	print("Error - Argumentos incorrectos")
	print("Ejemplo:decomposicion.py [0-9999]")
