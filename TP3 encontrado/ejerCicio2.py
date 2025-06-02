#✅ 2. Clasificar edades ingresadas
#Enunciado: Ingresar edades hasta que se ingrese 0 
#y clasificar cuántos son niños (<13), adolescentes (13–17) y adultos (18+).
 
while True:
    Edad = int(input("Ingrese su edad"))
    if Edad < 13:
        print("Sos un niño")
    elif Edad >=18:
        print("Ya sos Adulto")
    else:
        print("Sos Adolescente")
    if Edad == 0:
        print("Ingrese realmente su edad")
        break
        