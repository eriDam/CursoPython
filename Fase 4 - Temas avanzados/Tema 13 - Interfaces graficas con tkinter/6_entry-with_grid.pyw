from tkinter import *

# Configuración de la raíz
root = Tk()

label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)#posicionar el cuadricula, cambiamos el pack x el grid

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal") #state puede ser disabled

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*") # muestra un carcater especial para que no se visualice


# Finalmente bucle de la apliación
root.mainloop()