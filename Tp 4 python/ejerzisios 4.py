# Ingreso de notas
notas = []
notas.append(int(input("Ingrese nota del primer alumno: ")))
notas.append(int(input("Ingrese nota del segundo alumno: ")))
notas.append(int(input("Ingrese nota del tercer alumno: ")))
notas.append(int(input("Ingrese nota del cuarto alumno: ")))
notas.append(int(input("Ingrese nota del quinto alumno: ")))
notas.append(int(input("Ingrese nota del sexto alumno: ")))
notas.append(int(input("Ingrese nota del séptimo alumno: ")))
notas.append(int(input("Ingrese nota del octavo alumno: ")))
notas.append(int(input("Ingrese nota del noveno alumno: ")))
notas.append(int(input("Ingrese nota del décimo alumno: ")))

# Contar aprobados y desaprobados
aprobados = 0
desaprobados = 0

for nota in notas:
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

# Mostrar resultados
print("Cantidad de alumnos aprobados:", aprobados)
print("Cantidad de alumnos desaprobados:", desaprobados)
