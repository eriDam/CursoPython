#1 Importamos el módulo
import sqlite3

# 2 Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# 3 Creamos el cursor para poder ejecutar código en formato SQL
# Lo utilizaremos para trabajar sobre la, base de datos y ejecutar nuestras consultas
cursor = conexion.cursor()

# 4 Consultamos la tabla 
cursor.execute("SELECT * FROM usuarios")
#print(cursor) # imprimir el cursor nos devolverá un registro codificado, hay que convertirlo en un objeto 

# 5 Recupera el primer registro
usuario = cursor.fetchone() # devuelve una tupla con el 1 reg, 
print(usuario[2]) # imprimimos la 3 posición(empieza en 0)
usuario = cursor.fetchone()# si lo volvemos a ejecutar mueve el cursor un elemento y muestra el siguiente


# 6 Guardamos los cambios haciendo un commit, tenemos que confrmar los cambios realizadospor seguridad.
conexion.commit()

# 7 Si ejecuto varias veces me realizará el mismo insert

# x Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()