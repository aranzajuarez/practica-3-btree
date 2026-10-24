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

    def insertar_hoja_simple(self, x):
        if self.raiz is None:
            self.raiz = NodoB(es_hoja=True)
            self.raiz.llaves.append(x)
            return

        # Insertar manteniendo las llaves ordenadas
        self.raiz.llaves.append(x)
        self.raiz.llaves.sort()