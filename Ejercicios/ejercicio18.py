# Ejercicio 18  Registro de cobros por vehículo


CAJONES = 5
tipos = ["Motocicleta", "Automóvil", "Camioneta", "Camión"]
tarifas = [10, 15, 20, 30]

registro = []
for i in range(CAJONES):
    registro.append(["LIBRE", "", "", "", "", ""])


def mostrar():
    print()
    print(f"{'Cajón':<6}{'Placa':<10}{'Tipo':<13}{'Entrada':<9}{'Salida':<8}{'Horas':<7}{'Importe'}")
    for i in range(CAJONES):
        f = registro[i]
        print(f"{i + 1:<6}{f[0]:<10}{f[1]:<13}{f[2]:<9}{f[3]:<8}{str(f[4]):<7}{str(f[5])}")


opcion = ""
while opcion != "4":
    print()
    print("1. Registrar entrada")
    print("2. Registrar salida y cobrar")
    print("3. Mostrar registro")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        
        cajon = -1
        for i in range(CAJONES):
            if registro[i][0] == "LIBRE" and cajon == -1:
                cajon = i
        if cajon == -1:
            print("No hay cajones libres.")
        else:
            placa = input("Placa: ").upper()
            for i in range(len(tipos)):
                print(f"{i + 1}. {tipos[i]} (${tarifas[i]}/h)")
            t = int(input("Tipo de vehículo (1-4): ")) - 1
            if t < 0 or t > 3:
                print("Tipo no válido.")
            else:
                entrada = input("Hora de entrada (HH:MM): ")
                registro[cajon] = [placa, tipos[t], entrada, "", "", ""]
                print(f"Vehículo asignado al cajón {cajon + 1}.")

    elif opcion == "2":
        placa = input("Placa que sale: ").upper()
        cajon = -1
        for i in range(CAJONES):
            if registro[i][0] == placa:
                cajon = i
        if cajon == -1:
            print("Vehículo no encontrado.")
        else:
            salida = input("Hora de salida (HH:MM): ")
            entrada = registro[cajon][2]
            min_ent = int(entrada[:2]) * 60 + int(entrada[3:])
            min_sal = int(salida[:2]) * 60 + int(salida[3:])
            if min_sal < min_ent:
                min_sal = min_sal + 24 * 60
            horas_reales = (min_sal - min_ent) / 60

            
            horas_cobradas = int(horas_reales)
            if horas_reales > horas_cobradas:
                horas_cobradas = horas_cobradas + 1
            if horas_cobradas == 0:
                horas_cobradas = 1

           
            tarifa = 0
            for i in range(len(tipos)):
                if tipos[i] == registro[cajon][1]:
                    tarifa = tarifas[i]
            importe = horas_cobradas * tarifa

            registro[cajon][3] = salida
            registro[cajon][4] = horas_cobradas
            registro[cajon][5] = importe

            print()
            print("----- COMPROBANTE DE SALIDA -----")
            print(f"Placa: {registro[cajon][0]}   Tipo: {registro[cajon][1]}")
            print(f"Entrada: {entrada}   Salida: {salida}")
            print(f"Permanencia: {horas_cobradas} h   Importe: ${importe}")
            print("---------------------------------")

            mostrar()
            
            registro[cajon] = ["LIBRE", "", "", "", "", ""]
            print(f"\nCajón {cajon + 1} liberado.")

    elif opcion == "3":
        mostrar()
    elif opcion == "4":
        print("Fin del programa.")
    else:
        print("Opción no válida.")
