"""
Este módulo presenta conceptos esenciales pero avanzados de Python relacionados con tipos de datos y estructuras de control.

- Tipos dinámicos y casting.
- Estructuras básicas: listas, tuplas, conjuntos y diccionarios.
- Comprensiones de listas y diccionarios.
- Pattern matching básico (PEP 634).
"""

# Ejemplo de tipos dinámicos: una variable puede cambiar de tipo en tiempo de ejecución
variable = 42
variable = "cuarenta y dos"  # Python permite cambiar el tipo de una variable libremente

# Listas y comprensión de listas
enumeros = list(range(10))
pares = [x for x in numeros if x % 2 == 0]  # Obtiene los números pares de 0 a 9

# Conjuntos y comprensión de conjuntos
unicos = {x % 3 for x in numeros}  # Produce {0, 1, 2}

# Diccionarios y comprensión de diccionarios
cuadrados = {x: x * x for x in range(5)}  # Crea un mapeo de números a su cuadrado

# Pattern matching (disponible desde Python 3.10)
def describir_numero(n: int) -> str:
    """Devuelve una descripción textual según el valor de n."""
    match n:
        case 0:
            return "cero"
        case 1 | 2:
            return "uno o dos"
        case _ if n < 0:
            return "negativo"
        case _:
            return "otro número"

# Ejemplo de uso de pattern matching
for i in [-1, 0, 1, 3]:
    descripcion = describir_numero(i)
    # Imprime la descripción correspondiente a cada número
    print(f"{i}: {descripcion}")

