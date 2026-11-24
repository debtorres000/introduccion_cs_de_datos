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
            
        elif tipo_vehiculo == "Automovil" or tipo_vehiculo == "automovil" or tipo_vehiculo == "AUTOMOVIL":
            tarifa = 15
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            
        elif tipo_vehiculo == "Camioneta" or tipo_vehiculo == "camioneta" or tipo_vehiculo == "CAMIONETA":
            tarifa = 20
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            
        elif tipo_vehiculo == "Camion" or tipo_vehiculo == "camion" or tipo_vehiculo == "CAMION ":
            tarifa = 30
            importe = horas * tarifa
            print(f"El total a pagar es: {importe} pesos")
            
        else:
            print("Error: Tipo de vehículo no reconocido.")
    print("="*30)
    continuar = input("¿Desea ingresar otro vehículo? (Escriba 'si' para continuar / Escriba 'no' para salir): ")
    
print("Jornada terminada. Sistema cerrado.")
