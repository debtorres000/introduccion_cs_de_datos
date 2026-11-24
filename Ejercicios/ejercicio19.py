# Ejercicio 19 (C). Reporte de ocupación e ingresos

FILAS = 3
COLUMNAS = 4
tipos = ["Motocicleta", "Automóvil", "Camioneta", "Camión"]
tarifas = [10, 15, 20, 30]

cajones = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append("LIBRE")
    cajones.append(fila)

ingresos_por_tipo = [0, 0, 0, 0]   # cuántos vehículos de cada tipo han entrado
atendidos = 0                      # vehículos que ya salieron y pagaron
total_ingresos = 0


def mostrar():
    print()
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if cajones[i][j] == "LIBRE":
                print(f"{'LIBRE':<8}", end=" ")
            else:
                print(f"{cajones[i][j][0]:<8}", end=" ")
        print()


opcion = ""
while opcion != "4":
    print()
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar entrada")
    print("2. Registrar salida y cobrar")
    print("3. Ver estacionamiento")
    print("4. Terminar jornada y mostrar reporte")
    opcion = input("Opción: ")

    if opcion == "1":
        fila = int(input(f"Fila (1-{FILAS}): "))
        col = int(input(f"Cajón (1-{COLUMNAS}): "))
        if fila < 1 or fila > FILAS or col < 1 or col > COLUMNAS:
            print("Posición no válida.")
        elif cajones[fila - 1][col - 1] != "LIBRE":
            print("Cajón ocupado.")
        else:
            placa = input("Placa: ").upper()
            for i in range(len(tipos)):
                print(f"{i + 1}. {tipos[i]} (${tarifas[i]}/h)")
            t = int(input("Tipo (1-4): ")) - 1
            if t < 0 or t > 3:
                print("Tipo no válido.")
            else:
                cajones[fila - 1][col - 1] = [placa, t]
                ingresos_por_tipo[t] = ingresos_por_tipo[t] + 1
                print("Entrada registrada.")

    elif opcion == "2":
        placa = input("Placa que sale: ").upper()
        encontrado = False
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if cajones[i][j] != "LIBRE" and cajones[i][j][0] == placa and not encontrado:
                    encontrado = True
                    t = cajones[i][j][1]
                    horas = float(input("Horas de estancia: "))
                    horas_cobradas = int(horas)
                    if horas > horas_cobradas:
                        horas_cobradas = horas_cobradas + 1
                    if horas_cobradas == 0:
                        horas_cobradas = 1
                    importe = horas_cobradas * tarifas[t]
                    total_ingresos = total_ingresos + importe
                    atendidos = atendidos + 1
                    cajones[i][j] = "LIBRE"
                    print(f"Importe a pagar: ${importe}. Cajón liberado.")
        if not encontrado:
            print("Vehículo no encontrado.")

    elif opcion == "3":
        mostrar()

    elif opcion == "4":
        
        ocupados = 0
        libres = 0
        mayor_ocupacion = -1
        fila_mayor = 0
        print()
        print("=============== REPORTE DE LA JORNADA ===============")
        print("Vehículos que permanecen dentro:")
        hay_dentro = False
        for i in range(FILAS):
            ocupados_fila = 0
            for j in range(COLUMNAS):
                if cajones[i][j] == "LIBRE":
                    libres = libres + 1
                else:
                    ocupados = ocupados + 1
                    ocupados_fila = ocupados_fila + 1
                    hay_dentro = True
                    print(f"  - {cajones[i][j][0]} ({tipos[cajones[i][j][1]]}) "
                          f"en fila {i + 1}, cajón {j + 1}")
            if ocupados_fila > mayor_ocupacion:
                mayor_ocupacion = ocupados_fila
                fila_mayor = i + 1
        if not hay_dentro:
            print("  (ninguno)")

        # Tipo con mayor número de ingresos
        pos_max = 0
        for k in range(len(ingresos_por_tipo)):
            if ingresos_por_tipo[k] > ingresos_por_tipo[pos_max]:
                pos_max = k

        print(f"Espacios ocupados: {ocupados}   Espacios libres: {libres}")
        print(f"Total de vehículos atendidos (con salida): {atendidos}")
        print(f"Ingresos generados: ${total_ingresos}")
        if sum(ingresos_por_tipo) == 0:
            print("Tipo con más ingresos: (sin registros)")
        else:
            print(f"Tipo de vehículo con más ingresos: {tipos[pos_max]} "
                  f"({ingresos_por_tipo[pos_max]})")
        print(f"Fila con mayor ocupación: fila {fila_mayor} ({mayor_ocupacion} vehículos)")
        print("=====================================================")

    else:
        print("Opción no válida.")
