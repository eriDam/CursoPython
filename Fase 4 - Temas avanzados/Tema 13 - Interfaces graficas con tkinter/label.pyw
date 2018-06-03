from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

# Título de la ventana
root.title("Mi label")

# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto") 

 

frame = Frame(root, width=480, height=320)
 
#frame.pack() #empaqueta y distribuye a su manera el tamaño de los widgets

#label = Label(frame, text ="Hola label").pack(side="left") #no hace caso de ponerse a la izq por que le indicamos que se muestre en esa posición.
 #la fomra correcta de emplazar un widget donde queramos
 #label.place(x=100,y=100) # centrado
#label.place(x=0,y=0) # izq arriba 
#label.place(x=100,y=0) # centrado arriba
# si hacemos un pack en lugar de un place, la label tendrá el tamaño de la etiqueta
#label.pack()
# label = Label(frame, text ="Otra label").pack() 
# label = Label(frame, text ="Última label").pack(side="right") 

"""
#Si lo anclamos
Label(root, text ="Hola label").pack(anchor="nw")
label = Label(root, text ="Otra label")  
label.pack(anchor="center") 
Label(root, text ="Última label").pack(anchor="se")


label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)
"""

# Las etiquetas pueden contener imagenes
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")


# Finalmente bucle de la apliación
root.mainloop()
