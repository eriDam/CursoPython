# Campos de texto, equivalente a lafunción input pero gráficamente

from tkinter import *

# Configuración de la raíz
root = Tk()

#creamos un marco 1 para colocar los elementos
frame = Frame(root)
frame.pack()

# Cear una entrada, un objeto decalse entry dentro de root
#entry = Entry(root)
#creamos la label dentro del frame
entry = Entry(frame)
entry.pack(side="right")

#Una label arriba del campo de entrada
#label = Label(root, text="Nombre")

#creamos la label dentro del frame
label = Label(frame, text="Nombre")
label.pack(side="left") # empaquetar pasando un side para que lo coloque correctamente

#creamos un marco 2
frame2 = Frame(root)
frame2.pack(side="right")

label2 = Label(root, text="Apellidos")
label2.pack(side="left") 

entry2 = Entry(frame2)
entry2.pack(side="right")

# Finalmente bucle de la apliación
root.mainloop()