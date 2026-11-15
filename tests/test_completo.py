import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btree import ArbolB

def ejecutar_pruebas_obligatorias():
    print("------------------------------------------")
    print("   PRUEBAS OBLIGATORIAS (Sección 5.1)    ")
    print("------------------------------------------")

    # Prueba 1: Árbol vacío
    arbol = ArbolB()
    assert arbol.buscar(10) is False, "Error en Prueba 1"
    print("Prueba 1: Búsqueda en árbol vacío -> NOT_FOUND")

    # Prueba 2: Inserción sin split
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(10)
    assert arbol.raiz.llaves == [10, 20, 40], "Error en Prueba 2"
    print("Prueba 2: Inserción sin split -> [10 | 20 | 40]")

    # Prueba 3: Primer split de la raíz
    arbol.insertar(30)
    assert arbol.raiz.llaves == [30], "Error en Prueba 3 (raíz)"
    assert arbol.raiz.hijos[0].llaves == [10, 20], "Error en Prueba 3 (izq)"
    assert arbol.raiz.hijos[1].llaves == [40], "Error en Prueba 3 (der)"
    print("Prueba 3: Primer split de raíz -> [30] con hijos [10 | 20] y [40]")

    # Prueba 4: Búsqueda existente e inexistente
    assert arbol.buscar(20) is True, "Error en Prueba 4 (20)"
    assert arbol.buscar(30) is True, "Error en Prueba 4 (30)"
    assert arbol.buscar(99) is False, "Error en Prueba 4 (99)"
    print("Prueba 4: Búsquedas (20 -> FOUND, 30 -> FOUND, 99 -> NOT_FOUND)")

def ejecutar_secuencia_final():
    print("\n -----------------------------------------")
    print("   SECUENCIA FINAL REPRODUCIBLE (5.3)    ")
    print("-----------------------------------------")

    arbol = ArbolB()
    secuencia_insercion = [20, 40, 10, 30, 50, 60, 70, 5, 15, 25, 35, 45]
    for x in secuencia_insercion:
        arbol.insertar(x)

    print("\n Árbol resultante (Prueba 5)")
    arbol.imprimir_por_niveles()

    # Prueba 6: Duplicado
    arbol.insertar(35)
    print("\n Insertar duplicado 35 (Prueba 6)")
    arbol.imprimir_por_niveles()

    print(f"\nbuscar(35) -> {'FOUND' if arbol.buscar(35) else 'NOT_FOUND'}")
    print(f"buscar(99) -> {'FOUND' if arbol.buscar(99) else 'NOT_FOUND'}")

    # Eliminaciones (Pruebas 7, 8 y 9)
    for x in [25, 10, 70, 5]:
        arbol.eliminar(x)

    print("\n Árbol final tras eliminar las llaves25, 10, 70 y 5 (Pruebas 7, 8 y 9)")
    arbol.imprimir_por_niveles()

    print(f"\nbuscar(25) -> {'FOUND' if arbol.buscar(25) else 'NOT_FOUND'}")
    print(f"buscar(35) -> {'FOUND' if arbol.buscar(35) else 'NOT_FOUND'}")

if __name__ == "__main__":
    ejecutar_pruebas_obligatorias()
    ejecutar_secuencia_final()