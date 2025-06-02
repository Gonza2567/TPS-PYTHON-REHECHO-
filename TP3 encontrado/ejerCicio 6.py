contraseña = "1234567890"  # La contraseña debe ser una cadena, no un número
intentos = 3

for i in range(intentos):
    a = input("Ingrese la contraseña: ")

    if a == contraseña:
        print("¡Acertaste!")
        break  # Si acierta, termina el bucle
    else:
        print("No acertaste.")

if a != contraseña:
    print("Has agotado tus intentos.")
 