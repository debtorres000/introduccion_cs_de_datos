#Se implementó un algoritmo genético que busca encontrar la mejor combinación de características para obtener buenos resultados en un modelo de clasificación.
#El programa crea diferentes combinaciones, evalúa su precisión y selecciona las mejores. 
#Después realiza cruces y mutaciones para generar nuevas combinaciones, repitiendo el proceso hasta encontrar la opción con mejor rendimiento.
import random
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar conjunto de datos
datos = load_iris()
X = datos.data
y = datos.target

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Configuracion del algoritmo
num_caracteristicas = X.shape[1]
tam_poblacion = 10
generaciones = 20

# Crear individuos aleatorios
def crear_individuo():
    return [random.randint(0, 1)
            for _ in range(num_caracteristicas)]

# Evaluar aptitud
def fitness(individuo):
    indices = [i for i in range(len(individuo))
               if individuo[i] == 1]

    if len(indices) == 0:
        return 0

    modelo = DecisionTreeClassifier(random_state=42)

    modelo.fit(X_train[:, indices], y_train)

    predicciones = modelo.predict(X_test[:, indices])

    return accuracy_score(y_test, predicciones)

# Inicializar poblacion
poblacion = [
    crear_individuo() for _ in range(tam_poblacion)
]

# Ejecutar algoritmo genetico
for generacion in range(generaciones):

    poblacion.sort(key=fitness, reverse=True)

    nueva_poblacion = poblacion[:2]

    while len(nueva_poblacion) < tam_poblacion:

        padre1 = random.choice(poblacion[:5])
        padre2 = random.choice(poblacion[:5])

        # Crossover
        punto = random.randint(1, num_caracteristicas - 1)

        hijo = padre1[:punto] + padre2[punto:]

        # Mutacion
        for i in range(num_caracteristicas):
            if random.random() < 0.1:
                hijo[i] = 1 - hijo[i]

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

# Obtener mejor individuo
mejor = max(poblacion, key=fitness)

print("Mejor individuo:", mejor)
print("Caracteristicas seleccionadas:")

for i in range(len(mejor)):
    if mejor[i] == 1:
        print(datos.feature_names[i])

print("Fitness:", fitness(mejor))
