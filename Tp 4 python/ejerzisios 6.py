donaciones = []

print("Colecta")
print("Ingrese los montos donados. Ingrese 0 para finalizar.")

total = 0
mayor = 0
cantidad = 0

while True:
    monto = int(input("Monto donado: "))
    
    if monto == 0:
        break

    if monto > 0:
        donaciones.append(monto)
        total = total + monto
        cantidad = cantidad + 1

        if monto > mayor:
            mayor = monto

print("Total recaudado:", total)
print("Mayor donación:", mayor)
print("Cantidad de personas que donaron:", cantidad)
