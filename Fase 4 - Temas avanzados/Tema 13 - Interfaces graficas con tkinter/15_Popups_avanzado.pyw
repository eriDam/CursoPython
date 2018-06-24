#Popups son ventanas que sirven para informar al usuario o solicitar informacion rápida al usuario
#importar el widget MessageBox
from tkinter import *
from tkinter import messagebox as MessageBox #renombramos para llamarlo así
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


# Configuración de la raíz
root = Tk() 

def test():
	#MessageBox.showinfo("Titulo ventana","mensaje de información") # info
	#MessageBox.showwarning("Titulo ventana","mensaje de Alerta") # alerta
	#MessageBox.showerror("Titulo ventana","mensaje de Error") # alerta
	# Esto devuelve un resultado yes o no según loque apriete el usuario, lo guardo en una variable para poder utilizarlo en alguna acción
	#resultado = MessageBox.askquestion("Título ventana","¿Está seguro de que desea salir sin guardar?") # preguntar al usuario
	#if resultado == "yes":  # "no"
	#	root.destroy() # destruye la ejecución del programa
	# resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
	# Otra variante para hacer una pregunta
	# resultado = MessageBox.askyesno("Salir","¿Está seguro que desea salir sin guardar?")
	#if resultado:
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
	#if resultado:
	#	root.destroy()
	#color = ColorChooser.askcolor(title="Elige un color")
	#print(color)
	#ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
	#	filetypes=(("Fichero de texto","*.txt"),
	#		("Fichero de texto avanzado","*.txt2"),
	#		("Todos los ficheros","*.*")) )
	#print(ruta)
		# equivale a open('ruta','w')
	fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt") 
	if fichero is not None:
		fichero.write("Hola voy a escribir otra cosa!")
		fichero.close()


Button(root,text= "Clícame", command = test).pack()

# Finalmente bucle de la aplicación
root.mainloop()
