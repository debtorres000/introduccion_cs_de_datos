no_visitas = int(input("Ingrese el número de visitas: "))
tiempo = float(input("Ingrese el tiempo de estancia en horas: "))

if tiempo < 0:
    print("Error: El tiempo de estancia no puede ser negativo.")
elif no_visitas < 0:
    print("Error: El número de visitas no puede ser negativo.")
else:
    if tiempo <= 2:
        tarifa = 20
    elif tiempo <= 5:
        tarifa = 18   
    else:
        tarifa = 15

    if no_visitas > 10:
        tarifa = tarifa * 0.9  # Equivalente a restar el 10%
        print("Se aplicó un descuento del 10% en la tarifa regular.")
    
    # 4. Calcular y mostrar el total solo si los datos fueron válidos
    total = tiempo * tarifa
    print(f"El total a pagar es: {total} pesos")