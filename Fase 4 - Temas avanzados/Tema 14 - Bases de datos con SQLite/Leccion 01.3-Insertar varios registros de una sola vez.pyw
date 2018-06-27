#1 Importamos el módulo
import sqlite3

# 2 Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# 3 Creamos el cursor para poder ejecutar código en formato SQL
# Lo utilizaremos para trabajar sobre la, base de datos y ejecutar nuestras consultas
cursor = conexion.cursor()

# 4 Consultamos la tabla 
#cursor.execute("SELECT * FROM usuarios")
#print(cursor) # imprimir el cursor nos devolverá un registro codificado, hay que convertirlo en un objeto 

# 5 Recupera el primer registro
#usuario = cursor.fetchone() # devuelve una tupla con el 1 reg, 
#print(usuario[2]) # imprimimos la 3 posición(empieza en 0)
#usuario = cursor.fetchone()# si lo volvemos a ejecutar mueve el cursor un elemento y muestra el siguiente

# 6 Creo una lista con varios users, en forma de tuplas, el mismo objeto que nos devuelve la DB
usuarios = [('Mario', 51, 'mario@ejemplo.com'),
            ('Mercedes', 38, 'mercedes@ejemplo.com'),
            ('Juan', 19, 'juan@ejemplo.com'),
            ]

# 7 Forma de insertar de forma masiva  executemany ejecutar varios
# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

# 8 Guardamos los cambios haciendo un commit, tenemos que confrmar los cambios realizadospor seguridad.
conexion.commit()

# x Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()