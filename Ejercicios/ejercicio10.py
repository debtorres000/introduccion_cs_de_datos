# Ejercicio 10 . Historial de vehículos


placas = []

print("=== HISTORIAL DE VEHÍCULOS ===")
continuar = "s"
while continuar == "s":
    placa = input("Placa del vehículo que ingresa: ").upper()
    placas.append(placa)
    continuar = input("¿Registrar otro vehículo? (si/no): ").lower()


print(f"Historial del día ({len(placas)} vehículos):")
for i in range(len(placas)):
    print(f"{i + 1}. {placas[i]}")
