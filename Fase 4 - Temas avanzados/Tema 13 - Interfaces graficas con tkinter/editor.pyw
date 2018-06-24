from tkinter import *
from tkinter import filedialog as FileDialog # Alias por buenas prácticas

# 8 Creamos una variable global para almacenar la ruta del fichero, si la ruta está vacia sabremos que el fichero es nuevo
# al guardarlo tendremos que guardarlo con un nombre, si la ruta está establecida es que el fichero es existente

ruta = ""

# Configuración de la raíz
root = Tk() 


# 1 Titulo
root.title("Dev Editor")
root.wm_iconbitmap('devEditor.ico') #formato ico

# 6 Lógica
# 9 Implementamos la funcionalidad
def nuevo():
	global ruta # hacemos referencia a que ruta es una vaiable global
	mensaje.set("Nuevo fichero")
	# 10 Implementamos la funcionalidad, damos a ruta un valor vacío
	ruta = ""
	# 11 borrar el texto, le pasamos un flotante, indicamos que desde el primer caracter hasta el final del texto y end
	texto.delete(1.0, "end")
	root.title("Dev Editor")

def abrir():
	global ruta
	mensaje.set("Abrir fichero")
	# 12 
	ruta = FileDialog.askopenfilename(
	 	initialdir='.', 
		filetype=(("Ficheros de texto", "*.txt"),),# 13 hay que pasarle una , por que no se le puede pasar solo un tipo
		title="Abrir un fichero de texto") 
	 	
	# 14 Tenemos que comprobar si realmente es una ruta a un fichero
	if ruta != "":
		fichero = open(ruta, 'r') # 15 abrimos el fichero en modo de lectura
		contenido = fichero.read() # 16 leemos el contenido
		texto.delete(1.0, 'end') # 17 aseguramos de que esté vacío el texto, 
		texto.insert('insert', contenido) # 18 insertamos el contenido
		fichero.close() # 19 cerramos el fichero, paso importante
		root.title(ruta + "Mi editor") # 20 pondrá la ruta en el título de la ventana


def guardar():
	mensaje.set("Guardar fichero")
	if ruta != "":
		contenido = texto.get(1.0,'end-1c') #end-1c para que no agregue un salto de línea al final
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado correctamente")
	else:
		guardar_como()

def guardar_como():
	global ruta
	mensaje.set("Guardar fichero como")
	fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0,'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado correctamente")
	else:
		mensaje.set("Guardado cancelado")
		ruta = ""



# 2 Menú superior
# 7 enlazamos las funciones de la lógica a los comandos del menú
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command= root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# 4 Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1) #para que ocupe el ancho del padre
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# 5 Crear un monitor inferior que informará de la acción que está ocurriendo en la parte inferior
mensaje = StringVar()
mensaje.set("Bienvenido al devEditor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

# 3 Añadimos a root el menú bar
root.config(menu=menubar)


# Finalmente bucle de la aplicación
root.mainloop()
