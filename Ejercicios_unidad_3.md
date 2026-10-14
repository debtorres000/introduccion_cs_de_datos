# Ejercicios unidad 3

## 3.1. ¿Cuáles son los tres tipos de aprendizaje automático?

1. Aprendizaje supervisado: uso de  datos etiquetados para aprender a realizar predicciones. 
2. Aprendizaje no supervisado: utiliza datos sin etiquetas para encontrar patrones o agrupar elementos similares. 
3. Aprendizaje por refuerzo: un agente aprende por medio la interacción con su entorno, recibiendo recompensas o penalizaciones según sus acciones. 

## 3.2. ¿Cuáles son las dos técnicas principales del aprendizaje supervisado?

1. Clasificación: nos permite predecir una categoría. Un buen ejemplo es, clasificar un correo como spam o no spam.
2. Regresión: permite predecir un valor numérico. Por ejemplo, estimar el precio de una casa según sus características.

## 3.3. Similitudes y diferencias entre el aprendizaje supervisado y el no supervisado

Tres similitudes:

1. Ambos utilizan datos para encontrar información útil.
2. Ambos emplean algoritmos de aprendizaje automático.
3. Ambos nos ayudar a tomar decisiones y resolver problemas.

Tres diferencias:

| Aprendizaje supervisado | Aprendizaje no supervisado |
| --- | --- |
| Utiliza datos etiquetados. | Utiliza datos sin etiquetas. |
| Busca predecir una categoría o un valor. | Busca descubrir patrones o grupos. |
| Su aprendizaje se guía mediante respuestas conocidas. | No cuenta con respuestas correctas previamente establecidas. |

## 3.4. Elegir entre aprendizaje supervisado y no supervisado

Se utilizaría el aprendizaje supervisado, ya que  los datos ya contienen una etiqueta conocida la cuál es el estado de salud. Aparte se menciona  la relación entre el género, la edad y el estado de salud para clasificar nuevos casos.

## 3.5. Elegir entre aprendizaje supervisado y supervisado

En este  caso se utilizaría el aprendizaje no supervisado, ya que no existe una variable objetivo etiquetada, también se  podrían agrupar las personas según sus características para encontrar patrones y similitudes.

## 3.6. ¿Qué son los datos etiquetados y no etiquetados?

- Datos etiquetados: Son aquellos que contienen información de entrada y una respuesta o categoría conocida.
- Datos no etiquetados: contienen información de entrada, pero no una respuesta o categoría asignada.

Para identificarlos, se debe revisar si existe una columna que indique el resultado o la categoría que se quiere aprender a predecir.

## 3.7. Clasificar los algoritmos de aprendizaje automático

| Tipo de aprendizaje | Algoritmos |
| --- | --- |
| Supervisado | Support Vector Machines (SVM), K-Nearest Neighbors (KNN), regresión lineal, regresión logística y Naïve Bayes. |
| No supervisado | K-Means, redes adversariales profundas (Deep Adversarial Networks), agrupamiento jerárquico y análisis de componentes principales (PCA). |
| Por refuerzo | Q-Learning y Temporal Difference (TD). |

### 3.7.1. Aprendizaje supervisado

Se utiliza cuando los datos tienen ejemplos con respuestas conocidas. El algoritmo aprende de esos ejemplos para predecir resultados nuevos.

- SVM: separa los datos en categorías mediante una frontera de decisión.
- KNN: clasifica un dato según los datos más parecidos que tiene cerca.
- Regresión lineal: predice valores numéricos, como el precio de una casa.
- Regresión logística: predice la probabilidad de pertenecer a una categoría, como aprobar o reprobar.
- Naïve Bayes: calcula probabilidades para clasificar datos, por ejemplo, identificar si un correo es spam.

### 3.7.2. Aprendizaje no supervisado

Se utiliza cuando los datos no tienen respuestas previamente identificadas. El algoritmo busca patrones, grupos o relaciones por su cuenta.

- K-Means: agrupa datos que tienen características similares.
- Deep Adversarial Networks: pueden aprender patrones de los datos mediante redes neuronales que compiten entre sí.
- Agrupamiento jerárquico: forma grupos organizados en diferentes niveles.
- PCA (análisis de componentes principales): reduce la cantidad de variables conservando la mayor parte posible de la información relevante..

### 3.7.3 Aprendizaje por refuerzo

El algoritmo aprende mediante la interacción con un entorno, recibiendo recompensas o penalizaciones según sus acciones.

- Q-Learning: aprende qué acciones conviene realizar para obtener mayores recompensas.
- Temporal Difference (TD): aprende y actualiza sus estimaciones utilizando la información obtenida durante la interacción, sin tener que esperar siempre al resultado final.

## 3.8. ¿Qué es una prueba A/B? ¿Cómo se planea y qué se puede probar?

Es una técnica que compara dos versiones de un producto, página o aplicación para identificar cuál funciona mejor.

Para planificarlo:

1. Definir el objetivo de la prueba.
2. Crear dos versiones: A y B.
3. Dividir a los usuarios en grupos comparables.
4. Medir los resultados durante un periodo adecuado.
5. Comparar los resultados y elegir la versión con mejor desempeño.

Aplicaciones: se puede utilizar para probar diseños de páginas web, botones, anuncios, correos electrónicos, aplicaciones móviles y estrategias de venta.

## 3.9. Encontrar las reglas de asociación

Regla de asociación, elegimos los productos mantequilla y huevos.

Lo que analizaremos es:

(Mantequilla) - >(Huevos)

Primero tenemos que contar las apariciones:

- Transacciones con mantequilla: T1, T2, T4, T9 y T10 =  5.
- Transacciones con huevos: T1, T2, T5, T6, T7 y T10 = 6.
- Transacciones que contienen ambos productos: T1, T2 y T10 = 3.
- Total de transacciones = 10

La regla indica que queremos saber con qué frecuencia aparecen los huevos cuando una transacción contiene mantequilla.

## 3.10. Calcular soporte, confianza y lift

Datos del ejercicio 3.9 y la regla mantequilla → huevos.

1. Soporte 

Indica la proporción de transacciones que contienen ambos productos.

Soporte = 3/10 = 0.30

Resultado: 30 %.

2. Confianza 

Indica la proporción de transacciones con mantequilla que también contienen huevos.

Confianza = 3/5 = 0.60

Resultado: 60 %.

3. Lift

Compara la confianza de la regla con la frecuencia general de los huevos.

Lift = 0.60/6/10 = 1

Resultado: 1.

Resultados: el soporte es del 30 %, la confianza es del 60 % y el lift es 1. Esto nos muestra que, en estos datos, la presencia de mantequilla no muestra una asociación positiva ni negativa con la presencia de huevos según esta medida.

## 3.11. Construir un árbol de decisión para la política de promociones

Mantener o retirar los regalos y descuentos dependiendo de si la ganancia es de al menos el 30 %.

¿La ganancia es mayor o igual al 30 %?

Sí —>Mantener los regalos y descuentos.

No —>Retirar los regalos y descuentos.

## 3.12. Ventajas y desventajas de un árbol de decisión

Ventajas:

1. Es fácil de entender e interpretar.
2. Permite representar las decisiones de manera visual.
3. Puede trabajar con variables numéricas y categóricas.
4. Ayuda a explicar por qué se tomó una decisión.

Desventajas:

1. Puede haber un sobreajuste a los datos de entrenamiento.
2. Pequeños cambios en los datos pueden producir un árbol diferente.
3. Un árbol demasiado grande puede ser difícil de interpretar.
4. Puede cometer errores si los datos de entrenamiento no representan bien la realidad.

## 3.13. ¿Cuántos enfoques existen para el análisis de clústeres?

1. Clústeres jerárquicos: forman una estructura de grupos y subgrupos. Pueden comenzar con grupos individuales que se van uniendo o partir de un grupo que se va dividiendo.
2. Clústeres particionales: dividen los datos en un número determinado de grupos. Un ejemplo es K-Means.
3. Clústeres basados en densidad: identifican grupos en zonas donde hay una alta concentración de datos, como DBSCAN.
4. Otros enfoques: incluyen métodos basados en modelos y en distribuciones probabilísticas.

La cantidad exacta depende de cómo se clasifiquen las técnicas. 

## 3.14. ¿Cuántas técnicas existen en el agrupamiento jerárquico?

1. Aglomerativa: comienza considerando cada objeto como un grupo individual y va uniendo los grupos más similares hasta formar una estructura jerárquica.
2. Divisiva: comienza con todos los objetos en un mismo grupo y los divide progresivamente en grupos más pequeños.

## 3.15. Encontrar los dos objetos con la distancia euclidiana mínima

Los puntos que se dan en el ejercicio son:

- A=(6,9)
- B=(8,1)
- C=(1,9)
- D=(4,3)

La fórmula de la distancia euclidiana es:

d$\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$

Calculamos las distancias entre los pares de puntos.

Distancia entre A y B:
$d(A,B)=\sqrt{(8-6)^2+(1-9)^2}$

$d(A,B)=\sqrt{4+64}=\sqrt{68}\approx8.25$

Distancia entre A y C:

$d(A,C)=\sqrt{(1-6)^2+(9-9)^2}$

$d(A,C)=\sqrt{25}=5$

Distancia entre A y D:

$d(A,D)=\sqrt{(4-6)^2+(3-9)^2}$

$d(A,D)=\sqrt{40}\approx6.32$

Distancia entre B y C:

$d(B,C)=\sqrt{(1-8)^2+(9-1)^2}$

$d(B,C)=\sqrt{113}\approx10.63$

Distancia entre B y D:

$d(B,D)=\sqrt{(4-8)^2+(3-1)^2}$

$d(B,D)=\sqrt{20}\approx4.47$

Distancia entre C y D:

$d(C,D)=\sqrt{(4-1)^2+(3-9)^2}$

$d(C,D)=\sqrt{45}\approx6.71$

Los dos objetos con la distancia euclidiana mínima son $B=(8,1) y D=(4,3)$, con una distancia aproximada de 4.47 unidades.

### 3.16 — Tabla de distancias euclidianas

| Objeto | X1 | X2 | Distancia a A(1,1) |
| --- | --- | --- | --- |
| A | 1 | 1 | 0 |
| B | 6 | 5 | $\sqrt{41}\approx 6.40$ |
| C | 3 | 3 | $\sqrt{8}\approx 2.83$ |
| D | 3 | 3 | $\sqrt{8}\approx 2.83$ |
| E | 3 | 1 | 2 |
| F | 5 | 2 | $\sqrt{17}\approx 4.12$ |
| G | 1 | 8 | 7 |
| H | 1 | 3 | 2 |
| I | 1 | 9 | 8 |
| J | 4 | 3 | $\sqrt{13}\approx 3.61$ |

La distancia máxima es 8, entre los objetos A(1,1) e I(1,9).

## 3.17. Explicar los pasos del proceso de reconocimiento de patrones

Se requiere de distintas etapas las cuales son

1. Adquisición de datos:  recopilar y almacenar los datos que se van a analizar. Pueden obtenerse manualmente o mediante sensores y otros sistemas automáticos.

2. Preprocesamiento: preparar los datos para analizarlos. Se corrigen errores, se tratan los valores faltantes y se reduce el ruido que podría afectar los resultados.

3. Extracción o selección de características: se identifican las características más importantes de los datos. Se eliminan las que son irrelevantes o redundantes para facilitar el análisis.

4. Clasificación: se utiliza un modelo para identificar patrones y asignar una categoría a los datos. Algunos métodos que pueden utilizarse son los árboles de decisión, las redes neuronales artificiales y Naïve Bayes.

5. Posprocesamiento: se revisan y validan los resultados obtenidos para determinar qué tan confiables son las decisiones tomadas.
