import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btree import ArbolB

arbol = ArbolB()
for num in [20, 40, 10, 30, 50, 60, 70, 5, 15, 25, 35, 45]:
    arbol.insertar(num)

print("Árbol inicial (Prueba 5)")
arbol.imprimir_por_niveles()

# Prueba 7: Eliminar 25 (hoja sin underflow)
arbol.eliminar(25)
print("\n Después de eliminar 25 (Prueba 7)")
arbol.imprimir_por_niveles()

# Prueba 8: Eliminar 10 y 70 (reparaciones por redistribución/fusión)
arbol.eliminar(10)
arbol.eliminar(70)
print("\n Después de eliminar 10 y 70 (Prueba 8)")
arbol.imprimir_por_niveles()

# Prueba 9: Eliminar 5 (disminución de altura de la raíz)
arbol.eliminar(5)
print("\n Después de eliminar 5 (Prueba 9 - Raíz reducida)")
arbol.imprimir_por_niveles() 