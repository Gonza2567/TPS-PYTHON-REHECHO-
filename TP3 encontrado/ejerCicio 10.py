while True:
    print("Menú de Opciones")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        print("Has elegido la Opción 1.")
    elif opcion == "2":
        print("Has elegido la Opción 2.")
    elif opcion == "3":
        print("Has elegido la Opción 3.")
    elif opcion == "4" or opcion.lower() == "salir":
        print("Has elegido salir. El programa termina.")
        break  # Termina el bucle si se elige "Salir"
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 4.")