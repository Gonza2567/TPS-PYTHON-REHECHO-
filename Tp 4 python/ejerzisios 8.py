#✅ 8. Control de ejercicio semanal
#Enunciado: Registrar cuántos minutos de ejercicio realiza una persona cada día durante una semana. 
#Si el promedio diario es menor a 30 minutos, sugerir aumentar la actividad.

total = 0


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia in dias:
    minutos = float(int(input(f"Ingrese cuantos minutos de ejercicio hiciste el día {dia} ")))
    total = total+minutos
promedio = total/7
if promedio < 30:
    print("Sugerimos aumentar actividad")
else:
    print("Estás perfectamente bien")
    