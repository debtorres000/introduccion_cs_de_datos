# Ejercicio 17 Registro de vehículos por cajón


FILAS = 3
COLUMNAS = 4

cajones = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append("LIBRE")
    cajones.append(fila)

opcion = ""
while opcion != "4":
    print()
    print("1. Registrar vehículo en un cajón")
    print("2. Consultar dónde está una placa")
    print("3. Mostrar estacionamiento")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        fila = int(input(f"Fila (1-{FILAS}): "))
        col = int(input(f"Cajón (1-{COLUMNAS}): "))
        if fila < 1 or fila > FILAS or col < 1 or col > COLUMNAS:
            print("Posición no válida.")
        elif cajones[fila - 1][col - 1] != "LIBRE":
            print(f"Cajón ocupado por {cajones[fila - 1][col - 1]}.")
        else:
            placa = input("Placa: ").upper()
            cajones[fila - 1][col - 1] = placa
            print("Vehículo registrado.")

    elif opcion == "2":
        buscada = input("Placa a buscar: ").upper()
        encontrada = False
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if cajones[i][j] == buscada:
                    print(f"La placa {buscada} está en la fila {i + 1}, cajón {j + 1}.")
                    encontrada = True
        if not encontrada:
            print("Esa placa no se encuentra en el estacionamiento.")

    elif opcion == "3":
        for i in range(FILAS):
            for j in range(COLUMNAS):
                print(f"{cajones[i][j]:<8}", end=" ")
            print()

    elif opcion == "4":
        print("Fin del programa.")
    else:
        print("Opción no válida.")
