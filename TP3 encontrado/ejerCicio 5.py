a = int(input("Ingrese un número: "))

if a <= 1:
    print("El número no es primo")
else:
    es_primo = True
    for i in range(2, a):
        if a % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
