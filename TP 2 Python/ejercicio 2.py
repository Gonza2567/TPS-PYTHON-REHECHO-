#2. Conversor de unidades: Crea un programa que permita convertir una
#cantidad en una unidad de medida a otra. 
#Por ejemplo, puedes convertir libras a kilogramos, kilómetros a millas, o grados Celsius a Fahrenheit.

print("1. De Kilo a libras")
print("2. De kilómetros a Milla")
print("3. De Celcius a Fahrenheit")

Opcion = int(input("Elija una opción (1, 2 o 3): "))
if Opcion == 1:
    Kilo = int(input("Ingrese la cantidad de Kilos para convertir a Libras"))
    conv1 = Kilo * 2.20462
    print("La cantidad de Kilos es ", Kilo, "Y en libras sería ", conv1)

elif Opcion == 2:
    Kilometro = int(input("Ingresa la cantidad de Kilometros para convertir a Milla"))
    conv2 = Kilometro * 0.621371
    print("La cantidad de Kilometros es ", Kilometro, "Y en Millas sería, ", conv2)
    
elif Opcion == 3:
    Celcius = int(input("Ingrese la cantidad de Grados Celcius para convertir a Fahrenheit"))
    conv3 = (Celcius * 9/5) + 32
    print("La cantidad en Grados Celcius es", Celcius, "Y en Fahrenheit sería", conv3 )