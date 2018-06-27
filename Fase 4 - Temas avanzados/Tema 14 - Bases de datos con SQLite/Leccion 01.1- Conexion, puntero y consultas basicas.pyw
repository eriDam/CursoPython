"""
Creación de una tabla utilizando sintaxis SQL
Antes de ejecutar una consulta (query) en código SQL, tenemos que crear un cursor.

Una vez creada la tabla, si intentamos volver a crearla dará error indicándonos que esta ya existe.
"""
#1 Importamos el módulo
import sqlite3

# 2 Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# 3 Creamos el cursor para poder ejecutar código en formato SQL
# Lo utilizaremos para trabajar sobre la, base de datos y ejecutar nuestras consultas
cursor = conexion.cursor()

# 4 Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# 5 No podemos crear una tabla si ya existe la comento para realizar un insert
cursor.execute("INSERT INTO usuarios VALUES ('EriDev',35,'ecc@ejemplo.com')")

# 6 Guardamos los cambios haciendo un commit, tenemos que confrmar los cambios realizadospor seguridad.
conexion.commit()

# 7 Si ejecuto varias veces me realizará el mismo insert

# x Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()