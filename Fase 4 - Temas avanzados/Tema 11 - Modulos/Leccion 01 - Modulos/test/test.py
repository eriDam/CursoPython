import sys

#Se recomienda crear un script al princio con los inserts para que lo gestiones todo ,pero python ofrece un sistema mas sencillo para gestionar modulos. los paquetes, ver la siguiente leccion.
sys.path.insert(1,'..') #hacemos diferencia al directorio anterior
#sys.path.insert(1,'.')#hace referencia al directorio actual

# CTRL + B mostrará en la consola los directorios donde el interprete d python va a buscar
#print(sys.path)

# ['D:\\_hubiC\\CursoPython_Udemy\\CursoPython\\Fase 4 - Temas avanzados\\Tema 11 - Modulos\\Leccion 01 - Modulos\\test', 'C:\\ProgramData\\Anaconda3\\python36.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Sphinx-1.5.1-py3.6.egg', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\setuptools-27.2.0-py3.6.egg']
# [Finished in 0.2s]



#Tambien se puede importar solo la clase Saludo, pero al estar en el directorio anteriro si no se le indica fallará
# Hay que darle la ruta y comprobar
from saludos import Saludo

Saludo()
