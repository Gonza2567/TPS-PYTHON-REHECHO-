#3 
#este codigo nos ordena y quita elementos repetidos en la lista
print("Vector3: ORDENAR Y QUITAR ELEMENTOS REPETIDOS DEL VECTOR.")
print("-------------------------------------------------------")

# Inicializar
VEC = []  # Lista vacía

# Entradas
print("Ingrese número de elementos del vector:")
N = int(input())

# Proceso
if 1 <= N <= 200:
    for i in range(1, N + 1):
        elemento = int(input("Ingrese Entero {0}: ".format(i)))
        VEC.append(elemento)

    # Quitar elementos repetidos y ordenar
    lista_nueva = []  # Lista vacía para almacenar elementos únicos
    for elemento in VEC:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)

    lista_nueva.sort()  # Ordenamos la lista sin duplicados

    # Salida
    print("\nSALIDA:")
    print("-------------------------------------------------------")
    print(lista_nueva)
else:
    print("Error: El número de elementos debe estar entre 1 y 200.")