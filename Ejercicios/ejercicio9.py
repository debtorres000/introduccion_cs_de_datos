cont_motos = 0
cont_autos = 0
cont_camionetas = 0
cont_camiones = 0
total_recaudado = 0
capacidad_maxima = 30
vehiculos_ingresados = 0
continuar = "si"

while continuar == "si" and vehiculos_ingresados < capacidad_maxima:
    espacios_disponibles = capacidad_maxima - vehiculos_ingresados
    print(f"=== Registro de Vehículo (Espacios disponibles: {espacios_disponibles}) ===")

    placa = input("Ingrese la placa del vehículo: ").strip()
    print("Tipos de vehículos: Motocicleta, Automovil, Camioneta, Camion")
    tipo_vehiculo = input("Ingrese el tipo de vehículo: ")
    horas = float(input("Ingrese las horas de estancia: "))

    if horas < 0:
        print("Error: Las horas de estancia no pueden ser negativas.")
    else:
        tarifa = 0

        if tipo_vehiculo == "motocicleta":
            tarifa = 10
            cont_motos += 1
        elif tipo_vehiculo in ("automovil", "automóvil"):
            tarifa = 15
            cont_autos += 1
        elif tipo_vehiculo == "camioneta":
            tarifa = 20
            cont_camionetas += 1
        elif tipo_vehiculo in ("camion", "camión"):
            tarifa = 30
            cont_camiones += 1
        else:
            print("Error: Tipo de vehículo no reconocido.")

        if tarifa > 0:
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            total_recaudado += importe
            vehiculos_ingresados += 1

    print("=" * 30)

    if vehiculos_ingresados == capacidad_maxima:
        print("Importante: Se ha alcanzado la capacidad máxima de 30 vehículos. No es posible recibir más vehículos.")
    else:
        espacios_disponibles = capacidad_maxima - vehiculos_ingresados
        print(f"Quedan {espacios_disponibles} espacios disponibles.")
        continuar = input("¿Desea ingresar otro vehículo? (Escriba 'si' para continuar / Escriba 'no' para salir): ")

print("=== CORTE DE CAJA ===")
print(f"Número total de vehículos atendidos: {vehiculos_ingresados}")
print(f"Cantidad de motocicletas: {cont_motos}")
print(f"Cantidad de automóviles: {cont_autos}")
print(f"Cantidad de camionetas: {cont_camionetas}")
print(f"Cantidad de camiones: {cont_camiones}")
print(f"Importe total recaudado: {total_recaudado} pesos")
print("Jornada terminada. Sistema cerrado.")