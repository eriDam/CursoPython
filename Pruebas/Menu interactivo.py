# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:47:54 2018

@author: erika_000
"""

print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer, escribe una opción?
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola espero que lo estes pasando bien")
       # print("Hasta pronto!")
       # break
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el primer número: "))
        print("El resultado de la suma es: ", n1 + n2)
       # print("Hasta pronto!")
       # break
    elif opcion == '3':
        print("Hasta luego!")
        break
    else:
        print("Comando desconocido")