from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

# Título de la ventana
root.title("Mi label")
# redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico


frame = Frame(root, width=480, height=320)
 
frame.pack() 
 
 

# Finalmente bucle de la apliación
root.mainloop()
