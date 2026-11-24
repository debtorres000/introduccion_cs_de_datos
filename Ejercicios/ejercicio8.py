total_vehiculos = 0
cont_motos = 0
cont_autos = 0
cont_camionetas = 0
cont_camiones = 0
total_recaudado = 0

continuar = "si"

while continuar == "si":
    print("--- Registro de Vehículo ---")
    placa = input("Ingrese la placa del vehículo: ")
    print("Tipos de vehículos: Motocicleta, Automovil, Camioneta, Camion")
    tipo_vehiculo = input("Ingrese el tipo de vehículo: ")
    horas = float(input("Ingrese las horas de estancia: "))

    if horas < 0:
        print("Error: Las horas de estancia no pueden ser negativas.")
    else:
        if tipo_vehiculo == "Motocicleta" or tipo_vehiculo == "motocicleta" or tipo_vehiculo == "MOTOCICLETA":
            tarifa = 10
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            cont_motos = cont_motos + 1
            total_vehiculos = total_vehiculos + 1
            total_recaudado = total_recaudado + importe
            
        elif tipo_vehiculo == "Automovil" or tipo_vehiculo == "automovil" or tipo_vehiculo == "AUTOMOVIL":
            tarifa = 15
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            cont_autos = cont_autos + 1
            total_vehiculos = total_vehiculos + 1
            total_recaudado = total_recaudado + importe
            
        elif tipo_vehiculo == "Camioneta" or tipo_vehiculo == "camioneta" or tipo_vehiculo == "CAMIONETA":
            tarifa = 20
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            cont_camionetas = cont_camionetas + 1
            total_vehiculos = total_vehiculos + 1
            total_recaudado = total_recaudado + importe
            
        elif tipo_vehiculo == "Camion" or tipo_vehiculo == "camion" or tipo_vehiculo == "CAMION":
            tarifa = 30
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            cont_camiones = cont_camiones + 1
            total_vehiculos = total_vehiculos + 1
            total_recaudado = total_recaudado + importe
            
        else:
            print("Error: Tipo de vehículo no reconocido.")
            
    print("----------------------------------")
    continuar = input("¿Desea ingresar otro vehículo? (Escriba 'si' para continuar / Escriba 'no' para salir): ")

print("=== CORTE ===")
print(f"Total de vehículos atendidos: {total_vehiculos}")
print(f"Cantidad de motos: {cont_motos}")
print(f"Cantidad de autos: {cont_autos}")
print(f"Cantidad de camionetas: {cont_camionetas}")
print(f"Cantidad de camiones: {cont_camiones}")
print(f"Importe total recaudado: {total_recaudado} pesos")
print("Jornada terminada. Sistema cerrado.")