# Ejercicio 14  Registro de ocupación


FILAS = 4
COLUMNAS = 5

espacios = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append(0)
    espacios.append(fila)

print("=== REGISTRO DE OCUPACIÓN ===")
continuar = "s"
while continuar == "s":
    print()
    fila = int(input(f"Número de fila (1-{FILAS}): "))
    col = int(input(f"Número de espacio (1-{COLUMNAS}): "))

    if fila < 1 or fila > FILAS or col < 1 or col > COLUMNAS:
        print("Posición fuera del estacionamiento.")
    elif espacios[fila - 1][col - 1] == 0:
        espacios[fila - 1][col - 1] = 1
        print("Espacio asignado correctamente.")
    else:
        print("Ese espacio ya está ocupado. Seleccione otro lugar.")

   
    for i in range(FILAS):
        for j in range(COLUMNAS):
            print(espacios[i][j], end="  ")
        print()

    continuar = input("¿Registrar otro vehículo? (si/no): ").lower()
