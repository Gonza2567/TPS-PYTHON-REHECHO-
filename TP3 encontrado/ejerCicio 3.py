total = 0

while True:
    
    precio = int(input("Ingrese el precio del producto (0 para finalizar): "))
    
    if precio == 0:
        break
    
    # Sumamos el precio al total
    total += precio

# Si el total supera los 10.000, aplicamos el descuento
if total > 10000:
    total -= total * 0.10  # Aplicamos un 10% de descuento

print("El total a pagar es: {total}")
