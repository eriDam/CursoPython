from tkinter import *

# Crear la raiz

root = Tk() #creamos un componente Tk

# Podemos configurar al root
# Configuración de la raíz
# Título de la ventana
root.title("Mi ventana")
#redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico


frame = Frame(root, width=480, height=320)
#lado alinear a la derecha
#frame.pack(side='right')
frame.pack(fill='both', expand=1) # para rellenar del todo el contenedor y se expanda, para que ocuoel lo mismo ique el padre
#frame.pack(fill='y', expand=1) # para rellenar vertical el contenedor y se expanda, para que ocuoel lo mismo ique el padre
#frame.pack(fill='x', expand=1) # para rellenar horiz el contenedor y se expanda, para que ocuoel lo mismo ique el padre

#frame.pack(fill='bottom', anchor="e") #a la derecha este w west izq
#frame.pack(side='bottom')
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")





root.config(cursor="arrow") #cursor desde la raíz
root.config(bg="blue") #fondo desde la raíz
root.config(bd=15) #borde desde la raíz
root.config(relief="ridge") #cresta desde la raíz


# Finalmente bucle de la apliación
root.mainloop()