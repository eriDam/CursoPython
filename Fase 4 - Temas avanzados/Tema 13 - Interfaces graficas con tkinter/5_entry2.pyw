from tkinter import *

# Configuración de la raíz
root = Tk()

# Creamos un objeto de tipo entry

entry = Entry(root)
entry.pack(side = "right")

#Una label arriba del campo de entrada para informar del campo de texto
label = Label(root, text="Nombre")
label.pack(side = "left")


entry2 = Entry(root)
entry2.pack(side = "right")

#Una label arriba del campo de entrada para informar del campo de texto
label2 = Label(root, text="Apellidos")
label2.pack(side = "left")



# Finalmente bucle de la apliación
root.mainloop()
