"""Ejercicio 4.13: selección de características hacia atrás."""

import pandas as pd


nombres = ["relevante", "redundante", "irrelevante"]
datos = pd.DataFrame(
    [[0, 0, 0], [0, 0, 1], [1, 1, 0], [1, 1, 1]], columns=nombres
)
datos["clase"] = [0, 0, 1, 1]


def consistencia(indices):
    if not indices:
        return datos["clase"].value_counts().max() / len(datos)
    columnas = [nombres[i] for i in indices]
    grupos = datos.groupby(columnas)["clase"]
    mayorias = grupos.agg(lambda grupo: grupo.value_counts().max())
    return mayorias.sum() / len(datos)


def seleccionar():
    seleccionadas = list(range(len(nombres)))
    while len(seleccionadas) > 1:
        candidatos = [
            [i for i in seleccionadas if i != quitar]
            for quitar in seleccionadas
        ]
        mejor = max(candidatos, key=consistencia)
        if consistencia(mejor) < consistencia(seleccionadas):
            break
        # Aceptar un empate elimina una característica innecesaria.
        seleccionadas = mejor
    return seleccionadas


if __name__ == "__main__":
    seleccionadas = seleccionar()
    print("Características seleccionadas:", [nombres[i] for i in seleccionadas])
    print(f"Consistencia: {consistencia(seleccionadas):.2f}")
