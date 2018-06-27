"""
Campos autoincrementales
No siempre contaremos con claves primarias en nuestras tablas (como el DNI), sin embargo siempre necesitaremos uno para identificar cada registro y poder consultarlo, modificarlo o borrarlo.

Para estas situaciones lo más útil es utilizar campos autoincrementales, campos especiales que asignan automáticamente un número (de uno en uno) al crear un nuevo registro. Es muy útil para identificar de forma única cada registro ya que nunca se repiten.

En SQLite, si indicamos que un campo numérico entero es una clave primaria, automáticamente se tomará como un campo auto incremental. Podemos hacerlo fácilmente así:
"""
import sqlite3

conexion = sqlite3.connect('productos.db')

cursor = conexion.cursor()

# Las cláusulas not null indican que no puede ser campos vacíos
cursor.execute('''CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')

conexion.close()