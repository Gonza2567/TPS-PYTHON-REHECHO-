##1. Clasificación de edad en categorías
#Enunciado:  
#Ingresar la edad de una persona y mostrar en qué categoría está:
 #Menor de edad: menos de 18 años.
 #Adulto: entre 18 y 64 años.
 #Adulto mayor: 65 años o más.

##Objetivo: Aplicar condicionales anidadas y dobles condiciones. 

a = int(input("Ingrese su edad: "))
if a < 18:
    print("Usted es menor de edad")
elif a >= 65:
    print("Usted es un adulto mayor")
else:
    print("Usted es mayor de edad")