# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:53:25 2018

@author: erika_000

Funciones
"""
def saludar():
    print("Hola, este print se llama desde la funcion")
    
saludar()

def dibujar_tabla_del_5():
    for i in range(11):
        print("5 *",i," = ",i*5)

dibujar_tabla_del_5()

#Con format
def dibujar_tabla_del_5():
    for i in range(11):
        print("5 * {} = {} ".format(i,i*5))

dibujar_tabla_del_5()

#◙Para llamar a la variable, debemos  declararla
def test():
    n=10
print(n)


m=10
def test():
    print(m)

llamar_funcion = test()
print(llamar_funcion)
