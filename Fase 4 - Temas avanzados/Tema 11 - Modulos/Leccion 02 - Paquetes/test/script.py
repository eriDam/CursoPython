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

# Si ejecutamos lo anterior, nos dará error ModuleNotFoundError: No module named 'paquete'
# Por que no encuentra el paquete, habría que crear el directorio como en la lección anterior.
# Tenemos que instalar el paquete dentro d python,  hay que convertir en un paquete distribuible
# Ver siguiente lección.