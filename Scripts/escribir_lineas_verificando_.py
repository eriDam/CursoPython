import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce 2 argumentos solo")
    print("Ejemplo: escribir_lineas.py Texto 5")