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