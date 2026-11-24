# Ejercicio 16. Identificación de la fila con mayor ocupación

espacios = [
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
]

mayor = -1
fila_mayor = 0

print("=== OCUPACIÓN POR FILA ===")
for i in range(len(espacios)):
    ocupados = 0
    libres = 0
    for j in range(len(espacios[i])):
        if espacios[i][j] == 1:
            ocupados = ocupados + 1
        else:
            libres = libres + 1
    print(f"Fila {i + 1}: {ocupados} ocupados, {libres} libres")

    if ocupados > mayor:
        mayor = ocupados
        fila_mayor = i + 1

print()
print(f"La fila con mayor ocupación es la fila {fila_mayor} con {mayor} vehículos.")
