#2 
#Este codigo nos pide ingresar libremente cantidad y numero de temperaturas, 
#para luego calcular su promedio

print("Vector2: MEDIA DE TEMPERATURAS.")

# Inicializar
Suma = 0
Media = 0.0
C = 0
Temp = []  # Lista vacía para almacenar temperaturas

# Entradas
print("Ingrese cantidad de Temperaturas: ")
N = int(input())

# Proceso
for i in range(N):
    temperatura = float(input("Ingrese Temperatura {0}: ".format(i + 1)))
    Temp.append(temperatura)
    Suma += temperatura  # Puedes usar directamente la variable `temperatura`

Media = Suma / N  # División real

# Contar cuántas temperaturas son mayores o iguales a la media
for tempElement in Temp:
    if tempElement >= Media:
        C += 1  # Esta línea debe estar correctamente indentada

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("La media es", Media)
print("Total de temperaturas >= a la media es", C)
