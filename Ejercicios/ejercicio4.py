tiempo = float(input("Ingrese el tiempo de estancia en horas: "))
if tiempo < 0:
    print("Error: El tiempo de estancia no puede ser negativo.")

else:
    if tiempo <= 2:
        tarifa = 20
    elif tiempo <= 5:
        tarifa = 18   
    else:
        tarifa = 15


    total = tiempo * tarifa
    print(f"El total a pagar es: {total} pesos")
