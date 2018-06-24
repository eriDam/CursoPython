# Botones seleccionables, una única opción
from tkinter import *

# Creamos una función para que cuando se pulse un  button se ejecute un comando y devolver el valor seleccionado
def seleccionar():
	cadena = ""
	# comprobamos si el valor de leche es 1
	if (leche.get()):
		cadena += "Con leche\n"
	else:
		cadena += "Sin leche\n"
	if (azucar.get()):
		cadena += "y con azúcar\n"
	else:
		
		cadena += "y sin azúcar\n"

	#cuando se llame a seleccionar mostraremos el monitor pasandole la cadena que hemos generado
	monitor.config(text=cadena)
 
# Configuración de la raíz
root = Tk() #creamos un componente Tk
root.title("Botones seleccionables") # Título de la ventana
root.config(bd=15) # borde de la ventana

#creamos las variables
leche= IntVar() # 1 =si, 0 = no
azucar= IntVar() # 1 =si, 0 = no

#Crear una imagen para distribuir los widgets
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

#creamos un frame y añadimos en root y lo empaquetamos a la derecha
frame = Frame(root)
frame.pack(side="right") 

"""
#creamos la label y los checkbuttons dentro de root
Label(root, text="¿Como quieres el café?").pack()
Checkbutton(root, text ="Con leche", variable=leche,onvalue=1, offvalue=0).pack() # valor por defecto onvalue clicado offvalue desmarcado
Checkbutton(root, text ="Con azúcar",variable=azucar,onvalue=1, offvalue=0).pack()
"""

#creamos la label y los checkbuttons dentro del frame y anclamos a la izq por que el frame esta a la derecha y nos desplaza las etiquetas y botones
Label(frame, text="¿Como quieres el café?").pack(anchor="w")
Checkbutton(frame, text ="Con leche", variable=leche,onvalue=1, offvalue=0,command=seleccionar).pack(anchor="w") # valor por defecto onvalue clicado offvalue desmarcado
Checkbutton(frame, text ="Con azúcar",variable=azucar,onvalue=1, offvalue=0,command=seleccionar).pack(anchor="w")


#creamos una label para recuperar el valor seleccionado
monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()