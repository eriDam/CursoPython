"""
Claves únicas
El problema con las claves primarias es que sólo podemos tener un campo con esta propiedad, y si da la casualidad que utilizamos un campo autoincremental, ya no podemos asignarla a otro campo.

Para estos casos existen las claves únicas, que nos permiten añadir otros campos únicos no repetibles.

Podemos adaptar el ejemplo de los usuarios con un campo autoincremental que haga de clave primaria, y a su vez marcar el DNI como un campo único:
"""
import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')

cursor = conexion.cursor()

# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    dni VARCHAR(9) UNIQUE,
                    nombre VARCHAR(100), 
                    edad INTEGER(3),
                    email VARCHAR(100))''')

usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]

cursor.executemany("INSERT INTO usuarios VALUES (null, ?,?,?,?)", usuarios)

conexion.commit()
conexion.close()