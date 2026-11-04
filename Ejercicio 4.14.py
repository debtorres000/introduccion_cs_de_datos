#se realizó un método de selección de características mediante números aleatorios. 
#El programa recorre cada característica y genera un número entre 0 y 1; si el número es menor o igual a 0.5, la característica se selecciona. 
#Al final, se muestran las características elegidas, que serán las que se utilicen para el análisis de datos
import random

# Características del conjunto de datos
caracteristicas = [
    "Edad",
    "Horas de estudio",
    "Calificacion",
    "Asistencia",
    "Participacion"
]

# Conjunto de características seleccionadas
seleccionadas = []

# Método Hit and Trial
for caracteristica in caracteristicas:
    if random.random() <= 0.5:
        seleccionadas.append(caracteristica)

# Mostrar resultados
print("Caracteristicas seleccionadas:")

for caracteristica in seleccionadas:
    print(caracteristica)

print("Total seleccionadas:", len(seleccionadas))
