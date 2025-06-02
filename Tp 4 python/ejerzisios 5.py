#✅ 5. Control de stock en una tienda
#Enunciado: Llevar el control del stock ingresando la cantidad de artículos 
#vendidos hasta que el stock llegue 
#a cero o se ingrese "0" para finalizar. Mostrar alertas si queda menos del 10% del stock original.

stock_original = int(input("Ingrese la cantidad inicial de stock: "))
stock_actual = stock_original

print("Ingrese la cantidad de artículos vendidos en cada operación.")
print("Ingrese 0 para finalizar.")

while stock_actual > 0:
    vendidos = int(input("Artículos vendidos: "))

    if vendidos == 0:
        print("Finalizando registro de ventas.")
        break

    if vendidos > stock_actual:
        print("No hay suficiente stock para esa venta. Intente con una cantidad menor.")
        continue

    stock_actual -= vendidos

    if stock_actual == 0:
        print("Stock agotado.")
        break

    porcentaje_restante = (stock_actual / stock_original) * 100
    if porcentaje_restante < 10:
        print("Alerta: queda menos del 10% del stock original.")

print("Stock final:", stock_actual)
