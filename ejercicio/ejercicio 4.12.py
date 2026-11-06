import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
# Cargar el conjunto de datos
datos = load_iris()

# Obtener las características
X = datos.data

# Obtener la variable objetivo
y = datos.target

# Mostrar las características
print("Características disponibles:")
print(datos.feature_names)
# Crear una lista vacía para las características seleccionadas
caracteristicas_seleccionadas = []

# Obtener todas las características disponibles
caracteristicas_restantes = list(range(X.shape[1]))

# Establecer la puntuación inicial
mejor_puntuacion = 0

print("\nIniciando selección de características...")
# Repetir mientras existan características disponibles
while caracteristicas_restantes:

    mejor_caracteristica = None
    puntuacion_candidata = 0

    # Probar cada característica disponible
    for caracteristica in caracteristicas_restantes:

        seleccion_temporal = caracteristicas_seleccionadas + [caracteristica]

        X_temporal = X[:, seleccion_temporal]

        modelo = DecisionTreeClassifier(random_state=42)

        puntuacion = cross_val_score(
            modelo,
            X_temporal,
            y,
            cv=5,
            scoring='accuracy'
        ).mean()

        if puntuacion > puntuacion_candidata:
            puntuacion_candidata = puntuacion
            mejor_caracteristica = caracteristica

    # Comprobar si mejora el resultado
    if mejor_caracteristica is None or puntuacion_candidata <= mejor_puntuacion:
        break

    # Agregar la mejor característica
    caracteristicas_seleccionadas.append(mejor_caracteristica)
    caracteristicas_restantes.remove(mejor_caracteristica)

    mejor_puntuacion = puntuacion_candidata

    print("Característica seleccionada:",
          datos.feature_names[mejor_caracteristica])

    print("Precisión:", mejor_puntuacion)
    # Mostrar resultados
print("\nRESULTADOS FINALES")

print("Características seleccionadas:")

for i in caracteristicas_seleccionadas:
    print(datos.feature_names[i])

print("Precisión final:", mejor_puntuacion)
