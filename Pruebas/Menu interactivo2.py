# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:06:11 2018

@author: erika_000
"""
n1 = float(input("Introduce un nº: "))
n2 = float(input("Introduce un nº: "))

print("""Elije una opción del menú 
          1) Sumar dos números 
          2) Restar dos números
          3) Multiplicar dos números""")
opcion =  input("Introudce la opción: ") 
    
if opcion == "1":
    print("La suma de ",n1, "+", n2, "es", n1+n2)
elif opcion == "2":
    print("La resta de ",n1, "+", n2, "es", n1-n2)
elif opcion == "3":
    print("La multiplicación de ",n1, "+", n2, "es", n1*n2)
else:
    print("Elige una opción valida")