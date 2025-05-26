# Generador de contraseñas seguras: 
#Crea un programa que genere contraseñas seguras automáticamente. 
#El usuario podrá especificar la longitud y los 
#caracteres que desea incluir (letras, números, símbolos). 
#El programa generará una contraseña aleatoria que cumpla con los criterios especificados      
 
import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()"

longitud = int(input("Longitud de la contraseña: "))

usar_letras = input("¿Incluir letras? (s/n): ") == "s"
usar_numeros = input("¿Incluir números? (s/n): ") == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ") == "s"

caracteres = ""
if usar_letras:
    caracteres += letras
if usar_numeros:
    caracteres += numeros
if usar_simbolos:
    caracteres += simbolos

if caracteres == "":
    print("No hay caracteres para generar la contraseña.")
else:
    contraseña = ""
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    print("Contraseña:", contraseña)