# Guía de contenido de la presentación

## Presentación

Hola, me llamo Roger Brascó Garcés y bienvenidos a mi presentación del trabajo final de carrera. Hoy hablaremos sobre el producto tensorial de conjuntos dendroidales.

## Introducción
Una de las ideas inciciales del trabajo era encontrar una formula cerrada para el número de shuffles entre dos arboles, pero para entender que significa este numero, hace falta toda una teoria que presentaré en la primera parte de la presentacion. 
Esta primera parte quiero llegar a explicar que es el producto tensorial, para ello debo introducir unas nociones previas. Luego seguiré con un formalismo de árboles y su definición como opéradas coloreadas. y Así podré introducir la nocion de conjuntos dendroidales junto con su producto tensorial.
En la segunda parte de la presentación comentaré como he desarrollado un paquete de python para que ayude con el calculo del producto tensorial mediante los shuffles.

## Nociones previas

En este trabajo he necesitado las nociones de categorias y de funtores, que no explicaré por falta de tiempo y porque son comunes. Pero si hablaré sobre que son las opéradas y su extension como coloreadas.

__Slide - Opérada__

**SAS**

__Slide - Opérada coloreada__

Una operada coloreada extiende la definición de operada mediante la introducción de un conjunto de colores C. De tal manera que las entradas y la salida de una operación son colores del conjunto C. **SAS**


## Conjuntos dendroidales

__Slide - Formalismo de arboles__

Voy introducir un formalismo de arboles. Un árbol es un grafo no vacı́o,  finito, conexo y sin lazos. Pero lo que se hace es borrar los vertices que solo tienen un arista adjunta, y dejar alguno como el vertice w si se quiere. Los vertices restantes seran los vertices que forman el arbol. Se escoje un arista que la llamaremos raiz, por ejemplo la arista a. Las hojas o aristas externas son las que tienen un solo vertice adjunto (como e o f) y las aristas internas son todas las que quedan (como b o d). Cada vertice tiene un conjunto de aristas de entradas y un arista de salida, (inputs y output). Entonces definimos un arbol planar con raiz como un arbol con raiz dotado con un orden lineal fijo en los conjuntos de entradas de cada vertice.

__Slide - Arboles como operadas coloreadas__

**SAS**

__Slide - Categorias omegap y omega__

**SAS**

Sean S y T dos arboles, entonces los morfismos de estas categorias son los morfismos entre operadads coloreadas generadas por S y T

__Slide - morfismos en omegap y omega__

Dentro de este conjunto de morfismos se puede diferenciar entre caras internas o externas y degeneraciones. Por ejemplo, esta funcion es una inclusion de colores y de las operaciones generadoras del primer arbol, menos la operacion u que se envia a la operacion composicion v-r por la arista b.

__Slide - Conjuntos denroidales__

**SAS**

__Slide - Nervio dendroidal__

**SAS**

## Producto tensorial

__Slide - Boardman-Vogt__

**SAS**

Las relaciones i,ii indican que la funcion que envia la operada P al producto tensorial de BV PQ son morfismos de operadas para color d, y analogamente para iii,iv. La quinta relacion se llama la relacion de intercambio, donde se observa se aplica una permutacion en las entradas del vertice blanco de la operada P, para obtener el itercambio con el vertice negro de la operada Q. Observamos que las hojas han sido permutadas en el intercambio.

__Slide - Producto tensorial en dendroidal__

**SAS**

## Conjunto de shuffles

__Slide - Shuffles__

Finalmente, hay otra alternativa para encontrar el producto tensorial. para ello voy a explicar que son los shuffles.

**SAS**

Entonces, el conjunto de shuffles entre dos arboles es la colecion de todos los shuffles posibles. 


__Slide - Estructura orden parcial__

**SAS** Donde R_1 es el shuffle T sobre S y R_N es el shuffle S sobre T. Es decir, el shuffle R_1 se forma mediante una copia de S y en cada entrada de S poner una copia de T. **SAS**

__Slide - Producto tensorial de arboles__

**SAS** Donde la union no es disjunta ya que hay shuffles que son caras de otros shuffles.

__Slide - Numero de shuffles de shuffles__

Es intersante calcular el numero de shuffles. **SAS**. Encontrar una formula cerrada para esta funcion recurisva es un problema abierto ya que es muy complejo y solo se conoce una formula cerrada para el caso especial de arboles lineales. Un arbol lineal es un arbol cuyos vertices solo tienen una entrada. De esta manera, la funcion recursiva se reduce a la relacion inductiva que define el coeficiente binomial.

__Slide - Generar shuffles python__

Para acabar, he desarrollado un paquete de python para tratar con los arboles como operadas y generar el conjunto de shuffles. Tambien este paquete tiene una herramienta para prinitar los arboles en latex, como todos los que hay en el trabajo o en la presentacion. 

Voy a mostrar todos los shuffles de estos dos arboles.
**SAS**
Lo que podemos ver como primer shuffle es T sobre S.
Para poder generar el conjunto de shuffles que estais viendo, he disenyado un algoritmo de busqueda no informada que tiene un actuador. es decir, es un algoritmo que encuentra vertices donde les puedo aplicar la norma del intercambio y luego aplicar dicho intercambio. Durante el proceso del algoritmo voy guardando cada shuffle y sus parientes, asi, puedo formar la estructura de orden parcial dentro del conjunto de shuffles.
tambien he desarrollado un algoritmo que sigue la proposicion del numero de shuffles, asi podia validar que mi algoritmo que genera los shuffles fuera correcto, comparando el numero total de shuffles encontrados y el numero obtenido por la proposicion. 
Este paquete es util ya que funciona mediante la entrada de una descripcion completa de un arbol como operada coloreada. 

Como conclusión, encontrar todos los shuffles envez de calcular el producto tensorial entre conjuntos dendroidales es util si puedes usar programa informatico para que te ayude con los multiples de calculos, ya que como podeis ver por arboles que parecen senzillos generan muchas configuraciones distintas.

