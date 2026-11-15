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
    
    def eliminar(self, x):
        """Elimina la llave x del árbol B manteniendo todas sus propiedades."""
        if self.raiz is None:
            return

        # Si la llave no existe en el árbol, no hacemos nada
        if not self.buscar(x):
            return

        self._eliminar_recursivo(self.raiz, x)

        # Caso especial: si la raíz quedó vacía y tiene un único hijo, reducimos altura
        if len(self.raiz.llaves) == 0:
            if not self.raiz.es_hoja:
                self.raiz = self.raiz.hijos[0]
            else:
                self.raiz = None

    def _eliminar_recursivo(self, nodo, x):
        i = 0
        while i < len(nodo.llaves) and x > nodo.llaves[i]:
            i += 1

        # CASO 1: La llave x está en este nodo
        if i < len(nodo.llaves) and nodo.llaves[i] == x:
            if nodo.es_hoja:
                # Etapa A: Está en una hoja, simplemente la quitamos
                nodo.llaves.pop(i)
            else:
                # Está en un nodo interno
                hijo_izq = nodo.hijos[i]
                hijo_der = nodo.hijos[i + 1]

                # Regla de desempate 4: Preferir predecesor si hijo izquierdo tiene > 1 llave
                if len(hijo_izq.llaves) > 1:
                    predecesor = self._obtener_predecesor(hijo_izq)
                    nodo.llaves[i] = predecesor
                    self._eliminar_recursivo(hijo_izq, predecesor)
                    if len(hijo_izq.llaves) == 0:
                        self._reparar_underflow(nodo, i)

                # Si no, intentar sucesor si hijo derecho tiene > 1 llave
                elif len(hijo_der.llaves) > 1:
                    sucesor = self._obtener_sucesor(hijo_der)
                    nodo.llaves[i] = sucesor
                    self._eliminar_recursivo(hijo_der, sucesor)
                    if len(hijo_der.llaves) == 0:
                        self._reparar_underflow(nodo, i + 1)

                # Si ninguno tiene llaves de sobra, fusionar ambos hijos con x
                else:
                    self._fusionar(nodo, i)
                    self._eliminar_recursivo(hijo_izq, x)
                    if len(hijo_izq.llaves) == 0:
                        self._reparar_underflow(nodo, i)
            return

        # CASO 2: La llave x no está aquí; debemos bajar al hijo correspondiente
        if nodo.es_hoja:
            return

        self._eliminar_recursivo(nodo.hijos[i], x)

        # Al regresar de la recursión, verificamos si el hijo quedó en underflow (0 llaves)
        if len(nodo.hijos[i].llaves) == 0:
            self._reparar_underflow(nodo, i)

    def _obtener_predecesor(self, nodo):
        """Busca la llave más grande en el subárbol (siempre bajando a la derecha)."""
        actual = nodo
        while not actual.es_hoja:
            actual = actual.hijos[-1]
        return actual.llaves[-1]

    def _obtener_sucesor(self, nodo):
        """Busca la llave más pequeña en el subárbol (siempre bajando a la izquierda)."""
        actual = nodo
        while not actual.es_hoja:
            actual = actual.hijos[0]
        return actual.llaves[0]

    def _reparar_underflow(self, padre, idx_hijo):
        """Repara un hijo con 0 llaves intentando redistribuir o fusionando."""
        # 1. Intentar pedir prestado al hermano izquierdo (Regla de desempate 1)
        if idx_hijo > 0 and len(padre.hijos[idx_hijo - 1].llaves) > 1:
            self._redistribuir_desde_izquierda(padre, idx_hijo)
        # 2. Intentar pedir prestado al hermano derecho (Regla de desempate 2)
        elif idx_hijo < len(padre.hijos) - 1 and len(padre.hijos[idx_hijo + 1].llaves) > 1:
            self._redistribuir_desde_derecha(padre, idx_hijo)
        # 3. Ningún hermano puede prestar -> Fusionar (Regla de desempate 3)
        else:
            if idx_hijo > 0:
                # Fusionar con hermano izquierdo
                self._fusionar(padre, idx_hijo - 1)
            else:
                # Fusionar con hermano derecho
                self._fusionar(padre, idx_hijo)

    def _redistribuir_desde_izquierda(self, padre, idx_hijo):
        hijo = padre.hijos[idx_hijo]
        hermano_izq = padre.hijos[idx_hijo - 1]

        # La llave separadora del padre baja al inicio del hijo subocupado
        hijo.llaves.insert(0, padre.llaves[idx_hijo - 1])
        # La última llave del hermano izquierdo sube al padre
        padre.llaves[idx_hijo - 1] = hermano_izq.llaves.pop()

        # Si no son hojas, movemos también el último hijo del hermano izquierdo
        if not hermano_izq.es_hoja:
            hijo.hijos.insert(0, hermano_izq.hijos.pop())

    def _redistribuir_desde_derecha(self, padre, idx_hijo):
        hijo = padre.hijos[idx_hijo]
        hermano_der = padre.hijos[idx_hijo + 1]

        # La llave separadora del padre baja al final del hijo subocupado
        hijo.llaves.append(padre.llaves[idx_hijo])
        # La primera llave del hermano derecho sube al padre
        padre.llaves[idx_hijo] = hermano_der.llaves.pop(0)

        # Si no son hojas, movemos también el primer hijo del hermano derecho
        if not hermano_der.es_hoja:
            hijo.hijos.append(hermano_der.hijos.pop(0))

    def _fusionar(self, padre, idx_separador):
        """Combina hijos[idx_separador] + padre.llaves[idx_separador] + hijos[idx_separador + 1]."""
        hijo_izq = padre.hijos[idx_separador]
        hijo_der = padre.hijos[idx_separador + 1]

        # Bajamos la llave del padre al hijo izquierdo y pegamos las llaves del derecho
        hijo_izq.llaves.append(padre.llaves.pop(idx_separador))
        hijo_izq.llaves.extend(hijo_der.llaves)

        # Si tienen hijos, también los unimos
        if not hijo_izq.es_hoja:
            hijo_izq.hijos.extend(hijo_der.hijos)

        # Eliminamos la referencia al hermano derecho que ya fue absorbido
        padre.hijos.pop(idx_separador + 1)