from tkinter import *

# Configuración de la raíz
root = Tk()

#creamos un marco 1 para colocar los elements
frame = Frame(root)
frame.pack()

# Cear una entrada, un objeto decalse entry dentr ode root
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

label = Label(root, text="Apellidos")
label.pack(side="left") 

entry = Entry(frame2)
entry.pack(side="right")

# Finalmente bucle de la apliación
root.mainloop()