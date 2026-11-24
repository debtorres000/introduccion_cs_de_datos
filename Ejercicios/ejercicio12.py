# Ejercicio 12 . Control de ingresos y egresos


CAPACIDAD = 15
dentro = []

opcion = ""
while opcion != "5":
    print()
    print("===== CONTROL DE ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar vehículos dentro")
    print("4. Ver ocupación y espacios disponibles")
    print("5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        if len(dentro) >= CAPACIDAD:
            print("Estacionamiento lleno. No se permite el ingreso.")
        else:
            placa = input("Placa que ingresa: ").upper()
           
            repetida = False
            for p in dentro:
                if p == placa:
                    repetida = True
            if repetida:
                print("Esa placa ya está registrada dentro.")
            else:
                dentro.append(placa)
                print("Ingreso registrado.")

    elif opcion == "2":
        placa = input("Placa que sale: ").upper()
        posicion = -1
        for i in range(len(dentro)):
            if dentro[i] == placa:
                posicion = i
        if posicion == -1:
            print("Esa placa no está registrada. No se puede registrar la salida.")
        else:
            dentro.pop(posicion)
            print("Salida registrada.")

    elif opcion == "3":
        if len(dentro) == 0:
            print("No hay vehículos dentro.")
        else:
            print("Vehículos dentro:")
            for i in range(len(dentro)):
                print(f"  {i + 1}. {dentro[i]}")

    elif opcion == "4":
        print(f"Vehículos estacionados: {len(dentro)}")
        print(f"Espacios disponibles:   {CAPACIDAD - len(dentro)}")

    elif opcion == "5":
        print("Fin del programa.")
    else:
        print("Opción no válida.")
