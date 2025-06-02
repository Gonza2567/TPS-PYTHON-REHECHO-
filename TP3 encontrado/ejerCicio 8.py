cont = 0 

for i in range(1, 5):
    n = int(input(f"Ingrese el número {i}: "))

    if n % 2 == 0:
        cont += 1 

print("Hay", cont, "números pares.")

