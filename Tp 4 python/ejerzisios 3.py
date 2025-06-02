#✅ 3. Seguimiento de hábitos saludables
#Enunciado: Pedir al usuario registrar cuántos vasos de agua toma 
# por día durante una semana (7 días). 
#Al finalizar, calcular el promedio diario y recomendar aumentar el consumo si está por debajo de 8.

vasos_sem = []

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

for dia in dias:
    vasos = int(input(f"Ingrese vasos de agua tomados el {dia}: "))
    vasos_sem.append(vasos)

#Para calcular el promedio de la semana
total = sum(vasos_sem)
promedio = total / len(vasos_sem)

print("Tomaste en promedio", promedio)

if promedio < 8:
    print("Se recomienda aumentar el consumo diario de agua.")
else:
    print("Estás tomando una cantidad adecuada de agua.")
