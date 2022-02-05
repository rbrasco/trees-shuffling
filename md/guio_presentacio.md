# Guía de contenido de la presentación

## Presentación

Hola, me llamo Roger Brascó Garcés y bienvenidos a mi presentación del trabajo final de carrera. Hablaremos sobre el producto tensorial de conjuntos dendroidales.

## Introducción

La idea principal del trabajo es entender que es este producto tensorial, para ello tengo que introducir unas nociones previas. 
Seguiré con un formalismo de árboles y su definición como opéradas coloreadas. Así podré introducir la nocion de conjuntos dendroidales y luego su producto tensorial. Finalmente hablaré de una técnica para encontrar dicho producto.

## Nociones previas

En este trabajo he necesitado las nociones de categorias y de funtores, que no explicaré por falta de tiempo y porque son comunes. Pero si hablaré sobre que son las opéradas y su extension como coloreadas.

__Slide - Opérada__

**SAS**

__Slide - Opérada coloreada__

Una operada coloreada extiende la definición de operada mediante la introducción de un conjunto de colores C. De tal manera que las entradas y la salida de una operación son colores del conjunto C. **SAS**


## Conjuntos dendroidales

__Slide - Formalismo de arboles__

Voy a dar un formalismo de arboles. Un árbol es un grafo no vacı́o,  finito, conexo y sin lazos. Pero lo que se hace es borrar los vertices que solo tienen un arista adjunta, y dejar alguno como el vertice w si se quiere. Los vertices restantes seran los vertices que forman el arbol. Se escoje un arista que la llamaremos raiz, por ejemplo la arista a. Las hojas o aristas externas son las que tienen un solo vertice adjunto (como e o f) y las aristas internas son las que quedan (como b o d). Cada vertice tiene un conjunto de aristas de entradas y un arista de salida, (inputs y output). Entonces un arbol planar con raiz es un arbol con raiz dotado con un orden lineal en los conjuntos de entradas de cada vertice.

__Slide - Arboles como operadas coloreadas__

**SAS**

__Slide - Categorias omegap y omega__

**SAS**

Sean S y T dos arboles, entonces los morfismos de estas categorias son los morfismos entre operadads coloreadas generadas por S y T

__Slide - morfismos en omegap y omega__

Dentro de este conjunto de morfismos se puede diferenciar entre caras internas o externas y degeneraciones. Por ejemplo, esta funcion es una inclusion de colores y de las operaciones generadoras del primer arbol, menos la operacion u que se envia a la composicion v-r por la arista b.

__Slide - Conjuntos denroidales__

**SAS**

__Slide - Nervio dendroidal__

**SAS**

## Producto tensorial

__Slide - Boardman-Vogt__

**SAS**

Las relaciones i,ii indica que la funcion que envia la operada P al producto tensorial de BV PQ son morfismos de operadas para color d, y analogamente para iii,iv. La quinta relacion se llama la relacion de intercambio, donde se observa se aplica una permutacion en las entradas del vertice blanco de la operada P, para obtener el itercambio con el vertice negro de la operada Q. Y las entradas son las mismas con otra configuracion planar.

__Slide - Producto tensorial en dendroidal__

**SAS**

## Conjunto de shuffles

__Slide - Shuffles__

Finalmente, hay otra alternativa para encontrar el producto tensorial. para ello voy a explicar que son los shuffles.

**SAS**

Entonces, el conjunto de shuffles entre dos arboles es la colecion de todos los shuffles posibles. 

__Slide - Conjunto de shuffles__

Es intersante calcular la cardinalidad del conjunto. **SAS**. Una de las ideas inciales del trabajo era ver si se puede encontrar una formula cerrada para esta funcion recurisva. Esto es un problema abierto ya que es muy complejo y solo se conoce una formula cerrada para el caso especial de arboles lineales. Un arbol lineal es un arbol cuyos vertices solo tienen una entrada. De esta manera, la funcion recursiva se reduce a la relacion inductiva que define el coeficiente binomial.

__Slide - Estructura orden parcial__

**SAS** Donde R_1 es el shuffle T sobre S y R_N es el shuffle S sobre T. Es decir, el shuffle R_1 se forma mediante una copia de S y en cada entrada de S poner una copia de T. **SAS**

__Slide - Producto tensorial de arboles__

**SAS** Donde la union no es disjunta ya que hay shuffles que son caras de otros shuffles.

__Slide - Generar shuffles python__

Para acabar, he desarrollado un paquete de python para tratar con los arboles como operadas y generar el conjunto de shuffles. Tambien este paquete tiene una herramienta para prinitar los arboles en latex, como todos los que hay en el trabajo o en la presentacion. 

**SAS**
Para poder generar el conjunto de shuffles he disenyado un algoritmo de busqueda no informada que tiene un actuador. es decir, es un algoritmo que encuentra vertices donde les puedo aplicar la norma del intercambio y luego aplicar dicho intercambio. En el proceso del algoritmo voy guardando cada shuffle y sus parientes, es decir, para cada shuffle tengo sus parientes directos, y asi, puedo formar la estructura de orden parcial dentro del conjunto de shuffles, como habiamos visto en ejemplo.
tambien he desarrollado un algoritmo que sigue la proposicion del cardinal del conjunto, asi podia validar que mi algoritmo que genera los shuffles sea correcto, comparando el numero total de shuffles encontrados y el numero obtenido por la proposicion. 
Todo este paquete funciona mediante la entrada de una descripcion completa de un arbol como operada coloreada. Y como podeis ver, este gif lo he podido generar con mi código de manera automatica.

Como conclusión, esta técncia alternativa de encontrar el producto tensorial entre conjuntos dendroidales es util si los arboles son pequeños pero si son grandes, si o si se debe usar un programa informatico para que te ayude con los multiples de calculos.

