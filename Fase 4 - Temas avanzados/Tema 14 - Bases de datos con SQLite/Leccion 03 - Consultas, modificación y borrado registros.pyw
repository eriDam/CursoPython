import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')

cursor = conexion.cursor()

#cursor.execute("SELECT * FROM usuarios WHERE id=1")
# Buscamos por dni
#cursor.execute("SELECT * FROM usuarios WHERE dni ='33333333C'")
# Buscamos por los que tengan la edad de 27, previamente en el gestor de BD le modificamos la edad para que hayan dos con la misma
cursor.execute("SELECT * FROM usuarios WHERE edad = 27")
# usuario = cursor.fetchone()
# print(usuario)
# usuario = cursor.fetchone()
# print(usuario)

# Si hacemos un fetchall y lo guardamos en una variable usuarios, accedemos a todos
usuarios = cursor.fetchall()
print(usuarios)
conexion.commit()
conexion.close()