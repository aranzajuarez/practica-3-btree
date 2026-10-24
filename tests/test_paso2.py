import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btree import ArbolB

arbol = ArbolB()

# Insertar Prueba 2
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(10)

# Verificamos que las llaves estan ordenadas en la raíz
print("Llaves en raíz:", arbol.raiz.llaves) # Esperado: [10, 20, 40]

arbol.insertar(30) 

# Verificamos la estructura resultante
print("Llave en Raíz:", arbol.raiz.llaves)                    # Esperado: [30]
print("Hijo Izquierdo:", arbol.raiz.hijos[0].llaves)          # Esperado: [10, 20]
print("Hijo Derecho:", arbol.raiz.hijos[1].llaves)            # Esperado: [40]