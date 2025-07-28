"""
Funciones avanzadas en Python.

Este módulo aborda conceptos fundamentales y avanzados sobre funciones:

- Las funciones son objetos de primera clase y pueden asignarse a variables o pasarse como parámetros.
- Cierres (closures) que capturan el entorno léxico.
- Argumentos variables (`*args` y `**kwargs`) para recibir un número arbitrario de parámetros.
- Funciones lambda para crear funciones pequeñas de forma concisa.
"""

# Las funciones pueden asignarse a variables y ser tratadas como cualquier otro objeto

def saludo(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    return f"Hola, {nombre}"

# Asignamos la función a otra variable
mi_funcion = saludo
print(mi_funcion("Ana"))

# Ejemplo de cierre (closure): una función interna recuerda el valor de su entorno

def potencia(exponente: int):
    """Devuelve una función que eleva un número a la potencia dada."""
    def elevar(base: int) -> int:
        return base ** exponente
    return elevar

cuadrado = potencia(2)
cubo = potencia(3)
print(cuadrado(4))  # 16
print(cubo(2))      # 8

# Uso de *args y **kwargs para aceptar cualquier número de argumentos posicionales y de palabra clave

def mezclar(*args, **kwargs):
    """Devuelve una tupla con los argumentos posicionales y un diccionario con los argumentos nombrados."""
    return args, kwargs

print(mezclar(1, 2, 3, clave="valor", otro="dato"))

# Funciones lambda: se utilizan para funciones simples y anónimas, comunes en operaciones como sort, map o filter
lista_de_tuplas = [(2, 'b'), (1, 'a'), (3, 'c')]

# Ordenar por el primer elemento de cada tupla usando lambda
lista_de_tuplas.sort(key=lambda x: x[0])
print(lista_de_tuplas)

# Ordenar por el segundo elemento (cadena)
lista_de_tuplas.sort(key=lambda x: x[1])
print(lista_de_tuplas)

