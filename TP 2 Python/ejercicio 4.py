#Calculadora de presupuesto: Escribe un programa que ayude a 
 #gestionar el presupuesto personal. El usuario deberá ingresar sus ingresos 
 #y gastos, y el programa mostrará el saldo disponible. Además, puede proporcionar
 #estadísticas sobre los gastos, como el porcentaje del presupuesto asignado a cada categoría.

saldo = 10000
ing_ = int(input("Ingrese sus ingresos: "))
b = saldo + ing_  # Saldo total disponible
gast_ = int(input("Ingrese sus gastos: "))

if gast_ <= b:
    saldo_rest = b - gast_
    print("Quedan", saldo_rest, "de saldo restante")
else:
    print("Te has pasado del saldo disponible.")
