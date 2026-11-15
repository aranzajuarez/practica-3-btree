import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btree import ArbolB

arbol = ArbolB()

# Secuencia exacta de la Prueba 5 obligatoria
secuencia = [20, 40, 10, 30, 50, 60, 70, 5, 15, 25, 35, 45]
for num in secuencia:
    arbol.insertar(num)

print("\n Resultado Prueba 5: división y propagación hasta crear una nueva raíz")
arbol.imprimir_por_niveles()

# Prueba 6: Insertar llave repetida (35)
arbol.insertar(35)
print("\n Resultado Prueba 6: Insertar llave repetida (35)")
arbol.imprimir_por_niveles()