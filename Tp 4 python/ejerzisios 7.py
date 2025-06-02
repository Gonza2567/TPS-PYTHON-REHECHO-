# ✅ 7. Registro de temperaturas semanales
#Enunciado: Registrar las temperaturas máximas de una semana, 
#calcular la media, y mostrar cuántos días superaron los 30°C.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = []

total = 0
dias_calor = 0

for dia in dias:
    temp = float(int(input("Ingrese la temperatura que hubo el " + dia + ": ")))
    temperaturas.append(temp)
    total = total + temp
    if temp > 30:
        dias_calor = dias_calor + 1

media = total / 7

print("La temperatura media fue de:", media)
print("Cantidad de días con más de 30°C:", dias_calor)

        

