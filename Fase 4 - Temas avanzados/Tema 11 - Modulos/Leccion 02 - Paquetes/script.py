# Hacemos referencia al módulo (contenido del paquete)
from paquete.saludos import *

# Hacemos referencia al subpaquete y luego al módulo (contenido del subpaquete hola)
from paquete.hola.saludos import *
from paquete.adios.despedidas import Despedida

# Objeto de tipo Saludo
Saludo()
saludar() # llamo a la funcion

# Objeto de tipo Despedida
Despedida()