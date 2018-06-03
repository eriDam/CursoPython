#import saludos

#saludos.saludar()

# Otra forma de llamar al método para importar la función y 
# no tener que lalmar cada vez a saludos

#from saludos import saludar
#para importarlas todas de golpe, ponemos * y las importa todas
# from saludos import *
# saludar()


#Al crear una clase, tenemos que llama 1 al modulo para llamar a la clase
#import saludos

#Llamamos a la clase Saludo y creo un objeto, pero no lo guardo 
#saludos.Saludo()

#Tambien se puede importar solo la clase Saludo
from saludos import Saludo

Saludo()