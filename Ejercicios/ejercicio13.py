# Ejercicio 13  Distribución de espacios


FILAS = 4
COLUMNAS = 5


espacios = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append(0)
    espacios.append(fila)


espacios[0][1] = 1
espacios[1][3] = 1
espacios[2][0] = 1
espacios[2][4] = 1
espacios[3][2] = 1

print("=== DISTRIBUCIÓN DEL ESTACIONAMIENTO ===")
print("0 = libre, 1 = ocupado")

print("       ", end="")
for j in range(COLUMNAS):
    print(f"E{j + 1} ", end="")

for i in range(FILAS):
    print(f"Fila {i + 1}  ", end="")
    for j in range(COLUMNAS):
        print(f"{espacios[i][j]}  ", end="")
   
