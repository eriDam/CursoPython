import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# Borramos sin el WHERE
cursor.execute("DELETE FROM usuarios")

# Consultamos de nuevo los usuarios
usuarios = cursor.execute("SELECT * FROM usuarios").fetchall()
print(usuarios)

conexion.commit()
conexion.close()