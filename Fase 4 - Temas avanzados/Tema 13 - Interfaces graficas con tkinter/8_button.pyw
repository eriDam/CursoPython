# Interfaz para realizar una suma, resta,multiplicación y borrar
from tkinter import *

"""
Establece en el resultado r la suma, resta y multip. del n1 y n2, 
lo tenemos que castear para que no se reciba como cadena,
si no no se podrá operar
"""
def sumar():
	r.set( float(n1.get()) + float(n2.get()) )
	borrar()

def resta():
	r.set( float(n1.get()) - float(n2.get()) )
	borrar() #Llamamos a borrar para limpiar el campo despues de asignar le resultado

def producto():
	r.set( float(n1.get()) * float(n2.get()) )
	borrar()

# Para limpiar los campos una vez se realiza la operación
def borrar():
	n1.set("")
	n2.set("")

# Configuración de la raíz
root = Tk()
root.config(bd=15)

#Variables para almacenar 
n1 = StringVar() #es una cadena tendremos que cambiar le tipo en la función
n2 = StringVar()
r = StringVar()

#Etiquetas para los campos de texto, empaquetamos 
Label(root, text="Número 1").pack()
#campo de texto
Entry(root, justify="center", textvariable=n1).pack() # primer numero
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack() # segundo numero
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack() # resultado, desactivamos que se pueda editar el resultado
Label(root, text="").pack() #para poner un espacio entre las entradas de texto y los botones
#Creo los botones
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


# Finalmente bucle de la apliación
root.mainloop()