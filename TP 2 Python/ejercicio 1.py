#1. Calculadora de propinas: Escribe un programa que solicite al usuario 
#ingresar el total de la cuenta de un restaurante y el porcentaje de propina que desea dejar. 
#El programa deberá calcular el monto de la propina y mostrar el total a pagar, incluyendo la propina.

Cuenta = int(input("Ingrese la cuenta"))
Propina = int(input("Ingrese el porcentaje de la propina a dejar"))

Total = Cuenta * (Propina / 100)

print("El total a pagar sería: ", Total+Cuenta)
