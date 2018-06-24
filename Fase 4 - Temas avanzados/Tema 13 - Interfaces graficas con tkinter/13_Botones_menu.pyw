from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

# Título de la ventana
root.title("Menú ")
# redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico

menubar = Menu(root)
# El menú no e empaqueta, debe añadirse de forma manual a la raíz
root.config(menu=menubar)

# creamos los menús y los añadimos al menú bar
filemenu = Menu(menubar,tearoff=0) # para que no salga un submenu con -- por defecto le añadimos tearoff a 0
#Le añadimos un submenú
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
# Añadir separador utilizando add_separator
filemenu.add_separator()
filemenu.add_command(label="Salir",command= root.quit)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
 

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de ...")


# hay que indicar que los añada, así como el texto que va a formar el menú
menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Editar",menu=editmenu)
menubar.add_cascade(label="ayuda",menu=helpmenu)

# Finalmente bucle de la aplicación
root.mainloop()
