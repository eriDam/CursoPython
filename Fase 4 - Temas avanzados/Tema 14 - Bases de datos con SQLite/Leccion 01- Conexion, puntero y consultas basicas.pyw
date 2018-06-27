# Conexión a la base de datos, creación y desconexión
#1 Importamos el módulo
import sqlite3

# 2 Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')


# 3 Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()