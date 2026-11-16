# Práctica 3: Implementación de un Árbol B Acotado ($m = 4$)

Implementación desde cero de un Árbol B acotado de orden fijo $m = 4$ para almacenar llaves enteras sin valores asociados ni duplicados, siguiendo el enfoque *bottom-up*.

## 1. Lenguaje utilizado
La práctica se desarrolló usando Python.

## 2. Instrucciones para ejecutar el programa
Clonar el repositorio y ubicarse en la carpeta raíz del proyecto desde la terminal.

Seguido, importamos la clase ArbolB desde src/btree.py y ejecutamos las operaciones básicas de insertar, buscar, eliminar e imprimir por niveles, usando:

from src.btree import ArbolB

arbol = ArbolB()
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(10)
arbol.imprimir_por_niveles()

## 3. Instrucciones para ejecutar los casos de prueba
Debemos ejecutar "python tests/test_completo.py"

## 4. Explicación breve de la representación de un nodo;
Cada nodo contiene 3 carcateristicas o atributos principales:

1. Llave: Lista ordenada ascendentemente de enteros, donde dada nuestra prática su capacidad máxima es $m-1=3$.
2. Hijos: Nodos conectados a otros nodos hijos o subnodos, podemos admitir como máximo $m=4$ hijos.
3. Es_hoja: Valor booleano (True or False) que indica si el nodo se encuentra en el nivel inferior del árbol.

## 5. Explicación de qué significa m = 4 y por qué cada nodo admite máximo tres llaves;
El tener un orden $m=4$ nos indica la capacidad máxima de ramificación de nuestro árbol, es decir que cada nodo puede desencadenar o "apuntar" a máximo 4 hijos. Donde, las llaves van separando a los subárboles definidos por $m$, de tal manera que podemos tener a lo más 3 llaves, es decir $m-1$.

## 6. Explicación de cómo se decide qué hijo seguir durante una búsqueda;
Cuando estamos revisando un nodo, podemos tener las llaves ordenadas $[k_1,k_2,k_3]$, donde estamos buscando la llave $k_x$, como estan ordenadas ascendentemente, buscamos de izquierda a derecha hasta encontrar el primer índice tal que $k_x\leq k_i$, así llegamos a 3 casos:

1. $k_x==k_i$, encontramos el valor buscado. 
    
2. $k_x<k_i$ Descendemos por el hijo en la posición $i$, dado que estos valores son menores a $k_i$

3. $k_x>k_i$ El valor buscado e smayor a todas las llaves, por tanto descendemos hasta la última llave. 


## 7. Explicación de qué ocurre cuando un nodo alcanza cuatro llaves;

Si queremos insertar una llave en un nodo que ya contiene 3 llaves, tendremos un desbordamiento u overflow, dado que tendríamos $[k_1,k_2,k_3,k_4]$, para solucionarlo, dado que debemos cumplir que haya $m-1$ llaves, hacemos una división o split, es decir dividimos nuestro nodo en dos nodos independientes, promoviendo una de las llaves hacia el nodo padre. Si la división estaba en nuestra raíz del árbol, crearemos una nueva raíz y la altura del árbol se incrementaría en uno.

## 8. Explicación de la convención de promoción usada en la práctica;
Cuando tengamos un desbordamiento, promoveremos al nodo padre a la segunda llave central, es decir dado el overflow $[k_1,k_2,k_3,k_4]$, promovemos a $k_3$, obteniendo los nodos:
Izquierdo: $[k_1,k_2]$
Derecho: $[k_4]$

Y el nodo padre insertando a $k_3$.

## 9. Explicación breve de redistribución y fusión;

Cuando queremos eliminar una llave, puede suceder que dejemos a un nodo con 0 llaves (cuando el nodo es distinto de la raíz), así realizaremos un underflow o subocupación, dependiendo el caso:

1. Caso 1: Si alguno de sus hermanos (izquierdo o en su defecto; derecho) tienen más de una llave, alguno de estos cede una llave al padre y la llave separadora de este último baja al nodo subocupado. 

2. Caso 2: Si ningún hermano puede ceder llaves, se combina el nodo vacío, la llave separadora del padre y el hermano izquierdo (o en su defecto el derecho). Propagando una revisión hacia arriba al haberse eliminado una llave del padre. Si la raíz quedará vacía con un único hijo, ese hijo pasa a ser la nuea raíz.

## 10. Respuesta a las preguntas marcadas en esta guía.

1. ¿Por qué al insertar una llave nueva no podemos decidir el hijo únicamente comparando con la primera llave del nodo?
Los nodos de nuestro Árbol B son de orden $m=4$, así podemos tener hasta 3 llaves que definirán 4 intervalos distintos, si al insertar una llave $k_x$ sólo la comparamos con la primer llave podemos caer en dos casos:
a) $k_x<k_1$, entonces insertamos la llave a la izquierda de $k_1$, es decir en el primer intervalo
b) $k_x>k_1$, dado que podemos tener hasta 4 intervalos, no podemos decidir entre los 3 intervalos mayores, en cual debería de ir $k_x$, así que por eso no es suficiente comparar con la primera llave de nuestro nodo para decidir en que subárbol hay que insertar al valor.

2. ¿Por qué una búsqueda no debe recorrer todos los hijos de un nodo?
Al tener las llaves de un nodo ordenadas ascendentemente, tenemos 4 rangos bien definidos, así, basta con identificar a que intervalo pertenecerá una llave $k_x$ a insertar, no es necesario revisar todos los hijos, sólo encontrar el intervalo al que pertenece y descartar el resto. Logrando que la búsqueda descienda por una sola rama.