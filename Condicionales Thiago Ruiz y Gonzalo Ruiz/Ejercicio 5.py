#📆 5. Días de la semana laborales o no laborales
#Enunciado:  
#Ingresar un número del 1 al 7 representando un día de la semana (1: lunes, 7: domingo). Indicar si ese día es:
# Día laboral (1 a 5)
# Fin de semana (6 o 7)

#Objetivo: Uso de `Segun` o condicionales múltiples con validación de rangos


dia = int(input("Ingrese un número del 1 al 7 representando un día de la semana (1: lunes, 7: domingo): "))

if dia < 1 or dia > 7:
    print("Número no válido, ingrese un número entre 1 y 7.")
else:
    #Para ver si entra en un día de semana
    if dia >= 1 and dia <= 5:
        print("Es un día laboral.")
    else:
        print("Es fin de semana.")