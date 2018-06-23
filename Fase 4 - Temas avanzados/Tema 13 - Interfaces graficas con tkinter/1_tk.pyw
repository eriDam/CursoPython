#Base para crear todos los componentes
# ctrl + b para ejecutar

# 1º importar los widgets
from tkinter import *

# Crear la raiz

root = Tk() #creamos un componente Tk

# Podemos configurar al root

# Título de la ventana
root.title("Mi ventana")
# No redimensionable 0,0
root.resizable(1,1) # verdadero 1,1 y falso 0,0
#debe ser formato ico
root.wm_iconbitmap('hola.ico') 

# Cuando  ejecutamos un fochero Python, si estableces q se abra con python
# desde sublime la consola sirve de terminal, pero si ejecutamos el archivo con python
# se abrirá el programa con  la terminal, se puede renombrar el archivo como pyw para no mostral la terminal



# abajo del todo, el el último paso antes de poner en marcha nuestra interfaz
# este método sirve para que se ejecute continuamente y no se cierre
root.mainloop()