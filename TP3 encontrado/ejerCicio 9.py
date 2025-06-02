menor_a_cero = 0
mayor_o_igual_30 = 0

while True:
    temp = float(input("Ingrese una temperatura (o -100 para terminar): ")) 
    
    if temp == -100:
        break

    if temp < 0:
        menor_a_cero += 1
    

    elif temp >= 30:
        mayor_o_igual_30 += 1

print(f"Cantidad de temperaturas menores a 0: {menor_a_cero}")
print(f"Cantidad de temperaturas mayores o iguales a 30: {mayor_o_igual_30}")
