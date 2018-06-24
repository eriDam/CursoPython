# Botones para añadir comportamientos dinámicos a nuetsars interfaces
from tkinter import *

# Definimos una función para crear comportamientos, se la pasare a command  
def hola():
	print("Hola")
# Esta función se utilizará para que el botón responda gráficamente y no por consola
# al pulsar el botón, se creará un label de texto y aparacerá debajo del botón, tantas veces como pulsemos el btn
def crear_label():
	 Label(root,text="Label creada dinámicamente").pack()

# Configuración de la raíz
root = Tk() #creamos un componente Tk
root.title("Mi  ") # Título de la ventana

"""
Creamos un boton y le pasamos root para añadirlo a la raíz, 
le pasamos un texto para que muestre
y lo empaquetamos.

Añadimos un comportamiento, crear el parámetro command y a este commmand 
le tendremos que enviar una función, la definimos arriba y se la pasamos
"""
Button(root, text="Haz click para hola",command=hola).pack()
Button(root, text="Haz click",command=crear_label).pack()





# Finalmente bucle de la aplicación
root.mainloop()