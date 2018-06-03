from tkinter import *

# Crear la raiz

root = Tk() #creamos un componente Tk

# Podemos configurar al root

# Título de la ventana
root.title("Mi ventana")
# No redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico





#abajo del todo
root.mainloop()