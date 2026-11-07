# Ejercicio 4.19 — Matriz de distancias Manhattan
# Objetos: X1, X2, X3, X4, X5 con coordenadas (x, y, z)

datos = {
    "X1": (0, 1, 3),
    "X2": (5, 5, 9),
    "X3": (2, 7, 4),
    "X4": (6, 9, 0),
    "X5": (7, 3, 6),
}

def manhattan(p, q):
    return sum(abs(a - b) for a, b in zip(p, q))

nombres = list(datos.keys())
n = len(nombres)

matriz = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = manhattan(datos[nombres[i]], datos[nombres[j]])

print("Matriz de distancias Manhattan:\n")
print("      " + "".join(f"{nombre:>6}" for nombre in nombres))
for i, nombre in enumerate(nombres):
    fila = "".join(f"{matriz[i][j]:>6}" for j in range(n))
    print(f"{nombre:>4}  {fila}")

print("\nDistancias por pares:")
for i in range(n):
    for j in range(i + 1, n):
        print(f"d({nombres[i]},{nombres[j]}) = {matriz[i][j]}")
