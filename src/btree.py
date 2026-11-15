from collections import deque

class NodoB:
    def __init__(self, es_hoja=True):
        # Cada nodo guarda sus llaves (máximo 3) y sus hijos (máximo 4)
        self.llaves = []
        self.hijos = []
        self.es_hoja = es_hoja

class ArbolB:
    def __init__(self):
        # Como el árbol está vacío, la raíz es None
        self.raiz = None

    def buscar(self, x):
        return self._buscar_recursivo(self.raiz, x)

    def _buscar_recursivo(self, nodo, x):
        if nodo is None:
            return False

        # Buscar el primer índice donde x <= llave
        i = 0
        while i < len(nodo.llaves) and x > nodo.llaves[i]:
            i += 1

        # Si encontramos la llave en la posición actual
        if i < len(nodo.llaves) and nodo.llaves[i] == x:
            return True

        # Si es una hoja y no la encontramos, no existe en el árbol
        if nodo.es_hoja:
            return False

        # Si es nodo interno, continuar la búsqueda en el hijo correspondiente
        return self._buscar_recursivo(nodo.hijos[i], x)

    def insertar(self, x):
        # Si el árbol está vacío, creamos la raíz
        if self.raiz is None:
            self.raiz = NodoB(es_hoja=True)
            self.raiz.llaves.append(x)
            return

        # Buscamos en el árbol, si el elemento ya existe no lo agregamos
        if self.buscar(x):
            return

        # Inserción recursiva bottom-up
        resultado = self._insertar_recursivo(self.raiz, x)

        # Si la raíz se dividió, creamos una nueva raíz
        if resultado is not None:
            promovida, nodo_izq, nodo_der = resultado
            nueva_raiz = NodoB(es_hoja=False)
            nueva_raiz.llaves = [promovida]
            nueva_raiz.hijos = [nodo_izq, nodo_der]
            self.raiz = nueva_raiz

    def _insertar_recursivo(self, nodo, x):
        """Devuelve None si no hubo split, o (promovida, izq, der) si hubo split."""
        # CASO 1: Si estamos en una hoja, insertamos en orden
        if nodo.es_hoja:
            nodo.llaves.append(x)
            nodo.llaves.sort()

            # Comprobar si hay desbordamiento (4 llaves)
            if len(nodo.llaves) == 4:
                return self._split(nodo)
            return None

        # CASO 2: Si es nodo interno, buscamos por qué hijo bajar
        i = 0
        while i < len(nodo.llaves) and x > nodo.llaves[i]:
            i += 1

        resultado_hijo = self._insertar_recursivo(nodo.hijos[i], x)

        # Si el hijo no se dividió, no hacemos nada más
        if resultado_hijo is None:
            return None

        # Si el hijo se dividió, recibimos la llave promovida y los dos nuevos subnodos
        promovida, izq, der = resultado_hijo

        # Insertar la llave promovida y actualizar la lista de hijos en el nodo actual
        nodo.llaves.insert(i, promovida)
        nodo.hijos[i] = izq
        nodo.hijos.insert(i + 1, der)

        # Comprobar si este nodo (padre) también se desbordó
        if len(nodo.llaves) == 4:
            return self._split(nodo)
        return None

    def _split(self, nodo):
        # Convención: k3 (índice 2) es la promovida
        # Izquierdo conserva [k1, k2], Derecho conserva [k4]
        promovida = nodo.llaves[2]

        nodo_izq = NodoB(es_hoja=nodo.es_hoja)
        nodo_izq.llaves = nodo.llaves[0:2]

        nodo_der = NodoB(es_hoja=nodo.es_hoja)
        nodo_der.llaves = nodo.llaves[3:4]

        # Si no era hoja, repartimos también sus hijos
        if not nodo.es_hoja:
            nodo_izq.hijos = nodo.hijos[0:3]
            nodo_der.hijos = nodo.hijos[3:5]

        return promovida, nodo_izq, nodo_der

    def imprimir_por_niveles(self): #Imprime el árbol nivel por nivel de izquierda a derecha
        if self.raiz is None:
            print("Árbol vacío")
            return

        cola = deque([self.raiz])
        nivel = 0

        while cola:
            cantidad_nodos = len(cola)
            nodos_texto = []

            for _ in range(cantidad_nodos):
                nodo = cola.popleft()
                llaves_str = " | ".join(str(k) for k in nodo.llaves)
                nodos_texto.append(f"[{llaves_str}]")

                # Encolar hijos para el siguiente nivel
                for hijo in nodo.hijos:
                    cola.append(hijo)

            print(f"Nivel {nivel}: {' '.join(nodos_texto)}")
            nivel += 1