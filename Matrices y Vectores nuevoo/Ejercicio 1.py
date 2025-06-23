#1
#Este codigo nos muestra una lista de los elementos que el usuario ingrese 
#y la cantidad de elementos en la misma la elije el usuario.

print("Vector1: LECTURA DE N ELEMENTOS ENTEROS.")
#inicializar
i = 1
F = [] #Inicializamos una LISTA VACÍA
#Entrada
print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())
#Proceso
while i <= numElementos:
    elemento = int( input("Ingrese Elemento: "))
    F.append(elemento) #Agregamos el elemento a la lista
    i = i + 1
#Salida
print("\nSALIDA: ")
print(F) #Imprimimos la lista