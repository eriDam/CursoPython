import datetime #para conkseguir la hora actual
import time #para el programa unos instantes
import os #limpiart pantalla

while(True):
    os.system('cls')  # Limpiamos la pantalla
    dt = datetime.datetime.now()
    print( "{}:{}:{}".format( dt.hour, dt.minute, dt.second ) )
    time.sleep(1)