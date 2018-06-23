from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

# Título de la ventana
root.title("Mi label")

# Variables dinámicas, creamos un objeto de esta clase
texto = StringVar()
texto.set("Eri creando textos dinámicos") 

 

#frame = Frame(root, width=480, height=320)
 
#frame.pack() #empaqueta y distribuye a su manera el tamaño de los widgets

#label = Label(frame, text ="Hola label").pack(side="left") #no hace caso de ponerse a la izq por que le indicamos que se muestre en esa posición.
 #la fomra correcta de emplazar un widget donde queramos con place pasando una coordenada x e y
 #label.place(x=100,y=100) # centrado
#label.place(x=0,y=0) # esquina superior izq (arriba) 
#label.place(x=100,y=0) # centrado arriba
# si hacemos un pack en lugar de un place, la label tendrá el tamaño de la etiqueta
#label.pack()
# label = Label(frame, text ="Otra label").pack() 
# label = Label(frame, text ="Última label").pack(side="right") 

# comentario multilinea """
"""
#Si lo anclamos
Label(root, text ="Hola label").pack(anchor="nw")
label = Label(root, text ="Otra label")  
label.pack(anchor="center") 
Label(root, text ="Última label").pack(anchor="se")

# fg   cambia el color de la parte superior y la fuente
label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto) # le configuramos el stringVar, para que esté enlazada al texto dinámico
"""

"""
 Las etiquetas pueden contener imagenes, tKinter solo admite a través de la 
 clase PhotoImage 2 formatos
 gif y pgm
"""
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left") #borde 0 pixels y la empaquetamos y posicionammos dentro del contenedor


# Finalmente bucle de la apliación
root.mainloop()
