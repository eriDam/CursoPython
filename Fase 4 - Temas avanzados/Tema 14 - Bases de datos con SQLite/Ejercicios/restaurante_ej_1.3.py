"""
1.1) Vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:

Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.


1.2) Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es UNIQUE).

Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:

Primeros
Segundos
Postres

1.3) Crea una función llamada agregar_plato() que muestre al usuario las categorías disponibles y
 le permita escoger una (escribiendo un número).

Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, 
teniendo en cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

Agrega la nueva opción al menú de opciones y añade los siguientes platos:

Primeros: Ensalada del tiempo / Zumo de tomate
Segundos: Estofado de pescado / Pollo con patatas
Postres: Flan con nata / Fruta del tiempo
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
#Creo la funcion del ejercicio 1.2
def agregar_categoria():
	#Preguntará por teclado que se introduzca una nueva categoria
	categoria = input("¿Nombre de la nueva categoría?\n> ")
	# Una vez tenemos la categoría que ha introducido el usuario, creamos una nueva conexión
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()
	try:
	# Insertamos en la categoría la categoria leida
	#El primer campo es autoincremental y pondremos null, como es una cadena podemos utilizar el format pasandole la categoria 
	#que hemos leido de esta forma se insertará dinámicamente lacadena que le pasamos
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria) )
		#confirmamos con el commit
		conexion.commit()
		conexion.close()
	except sqlite3.IntegrityError:
		print("La categoria '{}' ya existe.".format(categoria))
	else:
		print("Categoría '{}' creada correctamente.".format(categoria))

# Crear la función agregar_plato() del ejercicio 1.3
def agregar_plato():
# Conexión a la bd	
		conexion = sqlite3.connect("restaurante.db")
		cursor = conexion.cursor()
# Muestra al usuario las categorias disponibles
		categorias = conexion.execute("SELECT * FROM categoria").fetchall() # hacemos directamente aquí el fetchall para devolver una lista
	 
		print("Selecciona una categoría para añadir el plato:")
		# hacemos un for para recorrer las categorías que hemos creado
		for categoria in categorias:
#Las mostramos de forma que el usuario interprete como si fuera el menú.
			print("[{}] {}".format(categoria[0],categoria[1])) # le pasamos con el format el primer elemento y el segundo que es el nombre

		# Hacemos un input para recibir la categoria que ha intrioducido el usuario y la guardamos en una var
# Lo convertimos a entero por que si no no lo vamos a poder comparar con el identificador de la categoria en la tabla
		categoria_usuario = int(input("> "))

		#Preguntará por consola que se introduzca una nuevo plato
		plato = input("¿Nombre del nuevo plato?\n> ")
	 
	 
		try:
	# Insertamos en la categoría la categoria leida
	#El primer campo es autoincremental y pondremos null, como es una cadena podemos utilizar el format pasandole el plato y el identificador de la categoria 
	#que hemos leido de esta forma se insertará dinámicamente la cadena que le pasamos
			cursor.execute("INSERT INTO plato VALUES (null, '{}', '{}')".format(plato,categoria_usuario) )
		#confirmamos con el commit
			conexion.commit()
			conexion.close()
		except sqlite3.IntegrityError:
			print("El plato '{}' ya existe.".format(plato))
		else:
			print("Plato '{}' creado correctamente.".format(plato))

 
	
	# Una vez tenemos el plato que ha introducido el usuario, creamos una nueva conexión
 
	
# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
	print("\nBienvenido al gestor del restaurante!")
	#leemos una opción
	opcion = input("\nIntroduce una opción:\n[1] Agregar una categoría\n[2] Agregar un plato\n[3] Salir del programa\n\n>  ")
	
	# Analizamos que tenemos en opción, en forma de cadena sin transformar a int
	if opcion == "1":
		agregar_categoria()
	# Agregamos la nueva opción al menú
	elif opcion == "2":
		agregar_plato()
	elif opcion == "3":
		break
	else:
		print("Opción incorrecta")
	

# Para ejecutar este programa sublime no permite introducir por consola, hay que abrir la consola en el directorio donde tenemos 
# el archivo .py y ejecutarlo desde ahí.
