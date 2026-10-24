import sys
import os

# Permitir que Python encuentre la carpeta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btree import ArbolB

# Creamos un nuevo árbol
arbol = ArbolB()

# Probamos búsqueda en árbol vacío 
print("Buscar 10 en árbol vacío:", arbol.buscar(10)) # Esperado: False

# Insertar 3 llaves sin desbordar
arbol.insertar_hoja_simple(20)
arbol.insertar_hoja_simple(40)
arbol.insertar_hoja_simple(10)

# Verificamos que las llaves estan ordenadas en la raíz
print("Llaves en raíz:", arbol.raiz.llaves) # Esperado: [10, 20, 40]

# Probar búsquedas
print("Buscar 20:", arbol.buscar(20)) # Esperado: True
print("Buscar 99:", arbol.buscar(99)) # Esperado: False