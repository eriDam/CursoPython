from tkinter import *

# Crear la raiz
# Configuración de la raíz
root = Tk() #creamos un componente Tk

# Título de la ventana
root.title("Mi label")
# redimensionable
root.resizable(1,1) # verdadero y falso
root.wm_iconbitmap('hola.ico') #formato ico


frame = Frame(root, width=480, height=320)
 
frame.pack() #empqueta y distribuye a su manera el tamaño de los widgets

label = Label(frame, text ="Hola label") 
 #la fomra correcta de emplazar un widget donde queramos
 #label.place(x=100,y=100) # centrado
#label.place(x=0,y=0) # izq arriba 
#label.place(x=100,y=0) # centrado arriba
# si hacemosun pack en lugarr tde un place, la label tendrá el tamaño de la etiqueta
label.pack()
 

# Finalmente bucle de la apliación
root.mainloop()
