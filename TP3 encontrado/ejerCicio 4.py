import random

numero = random.randint(1, 10)

for i in range(3):
    intento = int(input("Adivina el número (entre 1 y 10): "))
    if intento == numero:
        print("¡Adivinaste el número!")
        break
    else:
        print("No adivinaste.")
else:
    print("Perdiste. El número era {numero}.")