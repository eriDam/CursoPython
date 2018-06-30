"""
Modificando registros específicos
De forma similar al SELECT podemos utilizar la cláusula:

UPDATE tabla
SET columna1 = valor1, columna2 = valor2...., columnaN = valorN
WHERE [condicion]

"""
import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# Actualizamos un registro importantísimo: No olvidar la cláusula WHERE o podéis acabar actualizando todos los registros
cursor.execute("UPDATE usuarios SET nombre='Hector Costa', edad = 30 WHERE dni='11111111A'")

# Ahora lo consultamos de nuevo
cursor.execute("SELECT * FROM usuarios WHERE dni='11111111A'")
usuario = cursor.fetchone()
print(usuario)

conexion.commit()
conexion.close()