neg = 0 
pos = 0         
negc = 0        
posc = 0         

for i in range(1, 11):
    n = int(input(f"Ingrese el número {i}: ")) 
    if n < 0:
        negc += 1
        neg += n
    elif n > 0:
        posc += 1
        pos += n

# Calcular promedios
if posc > 0:  # Evitar división por 0
    pospr = pos / posc
else:
    pospr = 0

if negc > 0: 
    negpr = neg / negc
else:
    negpr = 0

print(f"Hay {posc} números positivos")
print(f"Hay {negc} números negativos")
print(f"El promedio de los números positivos es: {pospr}")
print(f"El promedio de los números negativos es: {negpr}")