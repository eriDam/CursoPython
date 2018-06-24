# Radio Button, botones radiales otro componente básico para añadir a la interfaz de un formulario
#son para dar al usuario la opción de elegir una opción entre varias
from tkinter import *

# Creamos una función para que cuando se pulse un radio buton se ejecute un comando
def seleccionar():
	#cuando se llame a seleccionar mostraremos el monitor recuperando el valor a través de la var opcion
	monitor.config(text="{}".format(opcion.get()))

def reset():
	opcion.set(None) # Establecemos la opcion a null para que no haya ningún valor y se borre la selección
	monitor.config(text="") #establecemos monitor con un nulo
# Configuración de la raíz
root = Tk() #creamos un componente Tk
root.title("RadioButton") # Título de la ventana

opcion = IntVar()  
"""
Crear 1 Radiobutton, por defecto viene clicado
Un radiobutton tiene un valor por defecto, todos forman una 
posible opción y esa posible opcion es la variable.
Creamos la variable y se la pasamos, hay que asignar 
un valor específico para cada una de las opciones, 
de esta forma tenemos en opcion el numero que hemos seleccionado, luego 
tendríamos que hacer un get para conseguir este valor
"""

Radiobutton(root, text="Opción 1",variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2",variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3",variable=opcion, value=3, command=seleccionar).pack()

# creamos la label
monitor = Label(root)
monitor.pack()

# Para reiniciar creamos un boton y le pasamos un comando a ejecutar, crearemos la función para resetar
Button(root, text="Reset", command=reset).pack()

# Finalmente bucle de la aplicación
root.mainloop()