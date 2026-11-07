# Unidad 4. Selección de características y medidas de distancia

## 4.1 ¿Cuál es la diferencia entre características numéricas y categóricas?

**Características numéricas:** representan números y sus valores pueden ser discretos o continuos. Con ellas tiene sentido hacer operaciones aritméticas.

**Características categóricas:** usan símbolos o etiquetas para representar los valores del dominio, no cantidades.

---

## 4.2 ¿En cuántas categorías se dividen las características numéricas? Elabora cada categoría con un ejemplo.

Los valores de los atributos numéricos pueden ser discretos o continuos. Hay dos tipos:

### 1. Escala de intervalo (Interval-Scaled)

La diferencia entre dos valores tiene un significado. Permite comparar diferencias entre valores, pero no establecer proporciones significativas.

**Ejemplo:** El tiempo o las fechas. La diferencia entre 1984 y 2000 es de 16 años, misma diferencia entre 2000 y 2016.

### 2. Escala de razón (Ratio-Scaled)

Este tipo de característica posee las mismas propiedades que las características de escala de intervalo. También permite establecer relaciones de proporción entre sus valores.

**Ejemplo:** Usaremos las velocidades: un automóvil que viaja a 100 km/h va al doble de velocidad que uno que viaja a 50 km/h.

**Nota:** La clave para diferenciarlas es identificar si el cero representa la ausencia real de aquello que se está midiendo.

---

## 4.3 ¿En cuántas categorías se dividen las características categóricas?

Se dividen en 2 categorías:

### 1. Nominal

El orden no tiene sentido. Solo se puede decir si dos valores son iguales o distintos; los operadores «menor que» y «mayor que» no aplican.

**Ejemplo:** El atributo Género (M/F), donde ningún valor es mayor que el otro.

Otros ejemplos son el color o la ciudad.

### 2. Ordinal

Los valores tienen un orden y los operadores de comparación sí tienen sentido.

**Ejemplo:** El atributo Grado, donde la calificación «A» es mayor que «B».

Otros ejemplos son el nivel educativo o una escala de satisfacción (baja, media, alta).

---

## 4.4 Dibuja un árbol de decisión donde, si la edad de una persona es mayor a 18, puede ir al cine, o de otro modo, no puede ir al cine.

```text
             ¿Edad > 18?
               /     \
             Sí       No
             |         |
         Puede ir   No puede ir
          al cine     al cine
```

---

## 4.5 ¿Cuál es la diferencia entre selección de características y extracción de características?

**Selección de características:** conserva la semántica. Su objetivo es encontrar el conjunto original de características del dataset.

**Extracción de características:** por su parte, puede conservar la semántica del dataset, pero sus cambios al conjunto no son reversibles. En este proceso los datos se transforman para proyectar un espacio nuevo.

---

## 4.6 ¿Cuáles son las principales categorías en la selección de características?

Existen tres formas principales de filtrar datos útiles para no saturar los sistemas analíticos:

### 1. Filtro (Filter)

Funciona como un colador básico. Selecciona la información basándose en las propiedades de los datos por sí solos, sin importarle qué algoritmo se vaya a utilizar después.

### 2. Envoltorio (Wrapper)

Realiza un proceso de ensayo y error. Pone a prueba distintas combinaciones de datos usando directamente el modelo de aprendizaje para ver cuál da el resultado más exacto.

### 3. Integrado (Embedded)

Es una combinación eficiente de los dos anteriores. Mientras el sistema procesa los datos y aprende, va decidiendo de forma automática qué información sirve y cuál debe ignorar.

---

## Ejercicio 4.7: ¿Cuáles son las principales ventajas y desventajas de los enfoques de selección de características basados en filtros, en envoltorios (wrappers) y en modelos integrados (embedded)?

| Criterio | Filtros (Filter) | Envoltorios (Wrapper) | Integrados (Embedded) |
|---|---|---|---|
| **Ventajas** | Enfoque sencillo. Más eficiente. | Las dependencias de características son consideradas. La retroalimentación de la clasificación del algoritmo es considerada, por lo que las características de mejor calidad son seleccionadas. | Combina las ventajas de los dos enfoques anteriores. |
| **Desventajas** | La retroalimentación de la clasificación del algoritmo no es considerada, por lo que las características seleccionadas pueden afectar la eficiencia del algoritmo. | Computacionalmente caro, comparado con el enfoque de filtrado. Puede resultar muy sobrecargado. | Uso específico en Machine Learning. |

---

## Ejercicio 4.8. Beneficios de la selección de características (Benefits of Feature Selection)

### Principales beneficios de la selección de características

La selección de características (Feature Selection) es una técnica utilizada en Ciencia de Datos y aprendizaje automático que permite identificar las variables más importantes de un conjunto de datos y eliminar aquellas que no aportan información relevante.

Sus principales beneficios son:

### 1. Reducción de la dimensionalidad

Disminuye la cantidad de características o variables de un conjunto de datos, facilitando su análisis y procesamiento.

### 2. Mejora del rendimiento del modelo

Permite que los modelos de aprendizaje automático trabajen con información más relevante, lo que puede mejorar sus resultados.

### 3. Prevención del sobreajuste (Overfitting)

Ayuda a reducir el riesgo de que un modelo aprenda demasiado los datos de entrenamiento y tenga dificultades para trabajar con datos nuevos.

### 4. Reducción del tiempo de procesamiento

Al utilizar menos características, se necesita menos tiempo y recursos computacionales para entrenar los modelos.

### 5. Mayor facilidad de interpretación

Permite identificar cuáles son las variables más importantes, haciendo que los resultados sean más fáciles de comprender.

### 6. Eliminación de información innecesaria

Evita utilizar características repetitivas, irrelevantes o que aportan poca información al análisis.

---

## Ejercicio 4.10: Introducción a los métodos de selección de características

### 1. Ganancia de información (Information Gain)

La ganancia de información se relaciona con la incertidumbre de la característica. Para dos características X e Y, la característica X será preferible si su ganancia de información es mayor.

### 2. Distancia (Distance)

La medida de distancia representa con qué eficacia una característica puede discriminar la clase. Es preferible la característica con alto poder de discriminación.

### 3. Dependencia (Dependency)

La medida de dependencia especifica qué tan unívocamente se puede determinar el valor de una clase a partir de una característica o un conjunto de ellas.

A mayor dependencia de una clase sobre la característica, menor es la incertidumbre; por lo tanto, esa característica es más preferible.

### 4. Consistencia (Consistency)

Una característica consistente es aquella que proporciona la misma estructura de clases que entregaría el subconjunto completo de características.

### 5. Precisión de clasificación (Classification Accuracy)

Las características que aumentan la precisión del modelo siempre son preferibles. La calidad de las características se mejora gradualmente usando la retroalimentación del modelo.

---

## Ejercicio 4.11: Clasificación de algoritmos

### Filter
- ANOVA
- Chi-square
- Pearson's correlation
- LDA

### Wrapper
- Backward elimination
- Forward selection
- Recursive feature elimination
- Memetic algorithm

### Embedded
- Lasso regression
- Ridge regression
- Regularized trees

---

## Ejercicio 4.15: Relevancia vs. Redundancia de características

**Relevancia de una característica (Feature Relevancy):**

La relevancia de una característica siempre está ligada al criterio de selección. Si incluso después de eliminar la característica, la dependencia en el subconjunto actual es igual a la del conjunto completo, la característica puede considerarse irrelevante y eliminarse de forma segura.

**Redundancia de una característica (Feature Redundancy):**

Una característica redundante es aquella que no añade ninguna información al subconjunto de características.

---

## 4.16 ¿Cuáles son los problemas (issues) de la selección de características?

### 1. Escalabilidad (Scalability)

Para ordenar las características por calidad, el algoritmo necesita todo el conjunto de datos en memoria hasta terminar. Con volúmenes muy grandes, esto exige mucha memoria y recursos. Es inevitable, porque para obtener buenas características hay que considerar todos los datos.

### 2. Estabilidad (Stability)

Un algoritmo estable debe dar los mismos resultados aunque haya pequeñas perturbaciones. Factores como la cantidad de datos, el número de características o su distribución pueden afectar la estabilidad.

### 3. Datos enlazados (Linked Data)

Los algoritmos suponen que las características son independientes e idénticamente distribuidas. En la realidad, pueden estar relacionadas entre sí.

**Ejemplo:** En redes sociales, un usuario está ligado a sus publicaciones, y estas, a su vez, a otros usuarios que les dan «like».

Manejar esto sigue siendo un reto abierto.

---

## 4.17 Clasificación de algoritmos

### 1. Algoritmos exhaustivos

Revisan todas las posibles soluciones.

### 2. Algoritmos basados en búsquedas aleatorias

Utilizan números aleatorios para encontrar soluciones.

### 3. Algoritmos basados en heurísticas

Utilizan estrategias para encontrar soluciones de manera eficiente.

---

## 4.19 Considera el siguiente conjunto de datos para calcular la distancia Manhattan entre cada objeto.

### Matriz de distancias Manhattan

|     | X1 | X2 | X3 | X4 | X5 |
|:---:|---:|---:|---:|---:|---:|
| **X1** | 0 | 15 | 9 | 17 | 12 |
| **X2** | 15 | 0 | 10 | 14 | 7 |
| **X3** | 9 | 10 | 0 | 10 | 11 |
| **X4** | 17 | 14 | 10 | 0 | 13 |
| **X5** | 12 | 7 | 11 | 13 | 0 |

### Distancias por pares

| Par de objetos | Distancia |
|---|---:|
| d(X1, X2) | 15 |
| d(X1, X3) | 9 |
| d(X1, X4) | 17 |
| d(X1, X5) | 12 |
| d(X2, X3) | 10 |
| d(X2, X4) | 14 |
| d(X2, X5) | 7 |
| d(X3, X4) | 10 |
| d(X3, X5) | 11 |
| d(X4, X5) | 13 |

**Implementación:** Este ejercicio se calculó utilizando Python. Consultar el código correspondiente en la rama del repositorio.

---

## 4.20 Distancia Euclidiana

La siguiente tabla muestra la distancia suprema calculada entre cada uno de los objetos del conjunto de datos.

### Matriz de distancias

| Objetos | X1 | X2 | X3 |
|:---:|---:|---:|---:|
| **X1** | 0 | 3 | 8 |
| **X2** | 3 | 0 | 5 |
| **X3** | 8 | 5 | 0 |

### Procedimiento de cálculo

El procedimiento consiste en calcular la diferencia absoluta para el eje X y el eje Y, seleccionando siempre el número mayor:

**D(X1, X2):**

\[
\max(|9-6|, |6-8|) = \max(3,2) = 3
\]

**D(X1, X3):**

\[
\max(|9-1|, |6-5|) = \max(8,1) = 8
\]

**D(X2, X3):**

\[
\max(|6-1|, |8-5|) = \max(5,3) = 5
\]

**D(X, X):** La distancia de cualquier objeto consigo mismo siempre resulta en 0.

---

**Fin de la Unidad 4.**
