"""
vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:

Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.
"""
import sqlite3

# creo duncion que creará la bd
def crear_bd():
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()
# intentamos ejecutar
	try:
		#creamos la primera tabla, triple ''' para saltos de linea en el code
		cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
	 # Si hay un fallo lo capturamos
	except sqlite3.OperationalError:
		print("La tabla de Categorías ya existe.")
	else: #caso de que todo funciona ok
		print("La tabla de Categorías se ha creado correctamente.")
 	
	try:
		cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya existe.")
	else:
		print("La tabla de Platos se ha creado correctamente.")
	 

	conexion.close()
#
# Crear la base de datos
crear_bd()
