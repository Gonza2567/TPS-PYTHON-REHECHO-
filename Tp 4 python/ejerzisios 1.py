lim = 20000
gastos = []

print("Calculadora de gastos mensuales")
print("Ingresa tus gastos. El programa terminará cuando se supere el límite.")

while True:
    entrada = input("Ingrese su gasto durante el mes: ")
    gasto = int(entrada) 
    gastos.append(gasto)
    total = sum(gastos)

    if total > lim:
        print("Has superado el límite presupuestado de" , lim)
        print("Total gastado:", total)
        break
