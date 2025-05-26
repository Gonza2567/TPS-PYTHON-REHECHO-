# 🚗 2. Verificación de velocidad permitida
#Enunciado:  
#Pedir al usuario que ingrese la velocidad de su vehículo y verificar si:
# Está dentro del límite permitido (hasta 60 km/h),
# Está en exceso leve (entre 61 y 80 km/h),
# Está en exceso grave (más de 80 km/h).  
#Mostrar un mensaje acorde a la situación.

#Objetivo: Usar operadores relacionales y múltiples condiciones.

Velocidad = int(input("Ingrese la velocidad a la que iba su vehículo:"))

if Velocidad <= 60:
    print("Estás dentro del límite permitido")
if Velocidad >80:
    print("Excedió el límite")
else:
    print("Exceso leve de Velocidad")
