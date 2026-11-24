# Ejercicio 15  Conteo de espacios disponibles


espacios = [
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
]

total = 0
ocupados = 0
libres = 0

for i in range(len(espacios)):
    for j in range(len(espacios[i])):
        total = total + 1
        if espacios[i][j] == 1:
            ocupados = ocupados + 1
        else:
            libres = libres + 1

porcentaje = ocupados / total * 100

print("=== OCUPACIÓN DEL ESTACIONAMIENTO ===")
print(f"Total de espacios:   {total}")
print(f"Espacios ocupados:   {ocupados}")
print(f"Espacios libres:     {libres}")
print(f"Porcentaje de ocupación: {porcentaje:.1f}%")
