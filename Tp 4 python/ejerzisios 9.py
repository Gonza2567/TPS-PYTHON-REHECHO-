# ✅ 9. Simulador de compras con límite diario
#Enunciado: Simular que una persona realiza compras durante un día, 
#con un límite máximo diario de \$20.000. No debe permitir seguir comprando si se supera ese valor.

compras = 0
limite = 20000

while True:
    comprando = int(input("Ingrese los gastos del día"))
    compras = compras + comprando
    if compras>limite:
        print("Superaste el presupuesto diario")
        break