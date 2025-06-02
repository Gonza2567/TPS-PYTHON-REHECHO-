#✅ 10. Control de combustible de un vehículo
#Enunciado: Simular la carga y consumo de combustible de un vehículo. 
#Ingresar cargas y consumos hasta que se indique detener. 
#Verificar si queda combustible suficiente para 50 km, considerando un consumo de 0.07 litros/km

while True:
    carga = float(input("Ingresá litros cargados (0 para salir): "))
    if carga == 0:
        break

    uso = float(input("Ingresá litros consumidos (0 para salir): "))
    if uso == 0:
        break

    combustible = carga - uso
    necesario = 50 * 0.07

    if combustible >= necesario:
        print("Alcanza para 50 km")
    else:
        print("No alcanza para 50 km")