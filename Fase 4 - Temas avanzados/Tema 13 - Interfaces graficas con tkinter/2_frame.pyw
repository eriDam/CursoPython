from tkinter import *

# Crear la raiz

root = Tk() #creamos un componente Tk

# Configuración del root
# Título de la ventana
root.title("Mi ventana")
#redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico

# Como vamos a introducir este marco dentro de la raíz, 
# Le pasamos la raíz como argumento y ya la tendremos dentro.
# Como, un frame por defecto no tiene tamaño se lo configuraremos
frame = Frame(root, width=480, height=320)

#Para empaquetarlo y que se distribuya dentro de la raíz, utilizamos pack
# le decimos al frame que se empaquete a si mismo dentro de la raíz

# Por defecto el pack lo alinea arriba y al centro, podemos cambiar de lado o rellenar todo
#lado alinear a la derecha
#frame.pack(side='right')
# redimensionar el widget, que rellene el ancho del padre, y verticalmente con y
# si no tenemos un tamaño fijo
frame.pack(fill='both', expand=1) # para rellenar del todo el contenedor y se expanda, para que ocupe  lo mismo que el padre
#frame.pack(fill='y', expand=1) # para rellenar verticalmente el contenedor y se expanda, para que ocupe lo mismo que el padre
#frame.pack(fill='x', expand=1) # para rellenar el ancho horiz el contenedor y se expanda, para que ocupe lo mismo que el padre

#frame.pack(fill='bottom', anchor="e") #e es a la derecha este, w west izq
#frame.pack(side='bottom')
# frame.config(root, width=480, height=320) #no es necesario usar el config ya que se lo pasamos con  el root
frame.config(cursor="pirate") # para que cambie a una calavera, arrow
frame.config(bg="lightblue") #cambia color de fondo
frame.config(bd=25) # tamaño de borde en pixels
frame.config(relief="sunken") # cambia el tipo de borde con relieve hundido, ridge = cresta





root.config(cursor="arrow") #cursor desde la raíz
root.config(bg="blue") #fondo desde la raíz
root.config(bd=15) #borde desde la raíz
root.config(relief="ridge") #cresta desde la raíz


# Finalmente bucle de la apliación
root.mainloop()