# 🏦 4. Cajero automático básico
#Enunciado:  
#Ingresar un valor de saldo y luego pedir que se ingrese un monto a retirar. Verificar:
# Si el monto es menor o igual al saldo, realizar la operación y mostrar saldo restante.
# Si el monto es mayor al saldo, mostrar mensaje de “fondos insuficientes”.

#Objetivo: Condicional simple con operadores lógicos.

Saldo = 10000
Retiro = int(input("Ingrese el monto a retirar:"))
Saldo_restante = Saldo-Retiro
if Retiro <= Saldo:
    print(Saldo-Retiro)
else:
    print("Fondos insuficientes")