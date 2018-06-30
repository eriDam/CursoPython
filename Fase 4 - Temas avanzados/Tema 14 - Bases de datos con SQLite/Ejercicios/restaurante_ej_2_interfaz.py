"""
2) En este ejercicios debes crear una interfaz gráfica con tkinter (menu.py) que muestre de forma elegante el menú del restaurante.

Tú eliges el nombre del restaurante y el precio del menú, así como las tipografías, colores, adornos y tamaño de la ventana.
El único requisito es que el programa se conectará a la base de datos para buscar la lista categorías y platos.
Algunas ideas: https://www.google.es/search?tbm=isch&q=dise%C3%B1o+menu+restaurantes

"""

import sqlite3
from tkinter import *

# Configuracion de la raíz
root = Tk()
root.title("Food Lover - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

# Título
Label(root, text="   Food Lover   ", fg="blue", font=("Verdana", 28, "bold italic")).pack()
# Subtítulo
Label(root, text="Menú del día", fg="lightblue", font=("Verdana", 24, "bold italic")).pack()

# Separación de categorías
Label(root, text="").pack()

#conectar a la base de datos
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la base de datos 
# Muestra al usuario las categorias disponibles
categorias = cursor.execute("SELECT * FROM categoria").fetchall()# hacemos directamente aquí el fetchall para devolver una lista
 	#recorremos las categorias	
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Verdana", 20, "bold italic")).pack()
	# Separación de categorías
	Label(root, text="").pack()
	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
	for plato in platos:# anidamos  dentro otro for para consultar los platos
		Label(root, text=plato[1], fg="grey", font=("Tahoma", 15, "italic")).pack()

conexion.close()

#Precio del menú
Label(root, text="12 € (IVA incl.)", fg="blue", font=("Verdana", 15, "italic")).pack(side="right")




#ejecutamos el bucle
root.mainloop()