import sqlite3

conexion = sqlite3.connect('productos.db')
cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM productos")

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
productos = cursor.fetchall()

# Ahora podemos recorrer todos los productos
for producto in productos:
    print(producto)

conexion.close()