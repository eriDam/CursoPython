# El text sirve para crear un campo de etxto, para trabajar cn un campo multilinea, crear comentarios, descripciones...
from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

 
texto = Text(root)
 
texto.pack()
# width escribir caracteres en horizontal, height lineas en vertical, padx
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red") # selectbackground es ara el color que saldrá cuando el texto esté seleccionado


# Finalmente bucle de la aplicación
root.mainloop()
