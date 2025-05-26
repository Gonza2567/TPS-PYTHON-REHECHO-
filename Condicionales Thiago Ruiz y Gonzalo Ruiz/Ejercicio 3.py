
# 🍔 3. Menú de restaurante (uso de `Segun`)
#Enunciado:  
#Mostrar al usuario un menú con 4 opciones:
#1. Hamburguesa
#2. Pizza
#3. Ensalada
#4. Salir  
#El usuario debe ingresar un número y el programa mostrará lo que eligió. Si elige 4, el programa termina.

#Objetivo: Aplicar estructura `Segun`, lógica de menú, validación simple.

while True:  #El bucle continuará hasta que el usuario elija salir
    print("Menú de opciones:")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Ensalada")
    print("4. Salir")

    
    opcion = int(input("Seleccione una opción (1-4): "))
    #La comida del usuario dependerá de la opción que él mismo elija
    if opcion == 1:
        print("Usted eligió Hamburguesa.")
    elif opcion == 2:
        print("Usted eligió Pizza.")
    elif opcion == 3:
        print("Usted eligió Ensalada.")
    elif opcion == 4:
        print("Saliendo... ¡Gracias por usar el menú!")
        break  # Sale del bucle y termina el programa
    else:
        print("Opción inválida, por favor ingrese un número entre 1 y 4.")
