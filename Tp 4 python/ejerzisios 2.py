#✅ 2. Control de carga de combustible
#Enunciado: Crear una aplicación que permita registrar varias cargas de 
#combustible en litros y calcular el total cargado, el promedio por carga, 
#y mostrar alertas si alguna carga fue inferior a 5 litros (sospecha de error o recarga mínima).

cargas = []

print("Control de Carga de Combustible")
print("Ingrese la cantidad de litros por carga (número entero). Escriba '0' para finalizar.")

while True:
    entrada = input("Litros cargados: ")
    litros = int(entrada)  # Asumimos que el usuario siempre ingresa un número válido

    if litros == 0:
        break

    cargas.append(litros)

    if litros < 5:
        print("Alerta: carga inferior a 5 litros (posible error o carga mínima)")


total = sum(cargas)
cantidad = len(cargas)

if cantidad > 0:
    promedio = total // cantidad  # División entera
    print("Resumen de cargas:")
    print("Total cargado:", total, "litros")
    print("Promedio por carga:", promedio, "litros")
else:
    print("No se registraron cargas.")
