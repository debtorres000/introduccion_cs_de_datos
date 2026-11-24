# Ejercicio 11. Búsqueda de vehículos


placas = []

print("=== REGISTRO DE PLACAS ===")
continuar = "s"
while continuar == "s":
    placas.append(input("Placa: ").upper())
    continuar = input("¿Registrar otra placa? (si/no): ").lower()

print()
print("=== BÚSQUEDA ===")
buscada = input("Placa a buscar en el historial: ").upper()


encontrada = False
posicion = -1
for i in range(len(placas)):
    if placas[i] == buscada:
        encontrada = True
        posicion = i
        break

if encontrada:
    print(f"La placa {buscada} SÍ está en el historial.")
    print(f"Posición en la lista: {posicion + 1} (índice {posicion})")
else:
    print(f"La placa {buscada} NO se encuentra en el historial.")
