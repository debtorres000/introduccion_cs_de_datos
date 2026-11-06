import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif

# Cargar el conjunto de datos
datos = load_iris()

# Obtener las características
X = datos.data

# Obtener la variable objetivo
y = datos.target

# Mostrar los nombres de las características
print(datos.feature_names)

# Seleccionar las 2 mejores características
selector = SelectKBest(score_func=f_classif, k=2)

# Aplicar la selección
X_nuevo = selector.fit_transform(X, y)

# Obtener los resultados
puntuaciones = selector.scores_

# Mostrar las puntuaciones
print("Puntuación de cada característica:")

for nombre, puntuacion in zip(datos.feature_names, puntuaciones):
    print(nombre, ":", puntuacion)
    # Mostrar las 2 mejores características seleccionadas

nombres_seleccionados = selector.get_support(indices=True)

print("\nCaracterísticas seleccionadas:")

for i in nombres_seleccionados:
    print(datos.feature_names[i])
