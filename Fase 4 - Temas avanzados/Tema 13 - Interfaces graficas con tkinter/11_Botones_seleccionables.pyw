# Botones seleccionables, una única opción
from tkinter import *

# Creamos una función para que cuando se pulse un  button se ejecute un comando
def seleccionar():
	#cuando se llame a seleccionar mostraremos el monitor recuperando el valor a través de la var opcion
	monitor.config(text="{}".format(opcion.get()))
 
# Configuración de la raíz
root = Tk() #creamos un componente Tk
root.title("Botones seleccionables") # Título de la ventana
root.config(bd=15) # borde de la ventana

#creamos las variables
leche= IntVar() # 1 =si, 0 = no
azucar= IntVar() # 1 =si, 0 = no

#creamos las etiquetas
Label(root, text="¿Como quieres el café?").pack()
Checkbutton(root, text ="Con leche", variable=leche,onvalue=1, offvalue=0).pack() # valor por defecto onvalue clicado offvalue desmarcado
Checkbutton(root, text ="Con azúcar",variable=azucar,onvalue=1, offvalue=0).pack()


# Finalmente bucle de la aplicación
root.mainloop()