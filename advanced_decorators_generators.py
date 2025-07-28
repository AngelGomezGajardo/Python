"""
Decoradores y generadores en Python.

Este módulo presenta:

- Decoradores para extender el comportamiento de funciones de manera modular.
- Generadores utilizando la palabra clave `yield` para producir secuencias de manera perezosa.
- Uso de `contextlib.contextmanager` para crear gestores de contexto personalizados con generadores.
"""

import functools
import time
from contextlib import contextmanager

# Decorador para medir el tiempo de ejecución de una función
def tiempo_de_ejecucion(funcion):
    """Imprime el tiempo que tarda en ejecutarse la función decorada."""
    @functools.wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@tiempo_de_ejecucion
def trabajo_pesado() -> int:
    """Función que realiza una suma grande para simular un trabajo intensivo."""
    total = 0
    for i in range(1_000_000):
        total += i
    return total

# Ejemplo de ejecución del decorador
if __name__ == "__main__":
    resultado = trabajo_pesado()
    print(f"Resultado: {resultado}")

# Generador simple que produce números enteros consecutivos
def contador_infinito():
    n = 0
    while True:
        yield n
        n += 1

# Uso de un generador
# for valor in contador_infinito():
#     if valor > 5:
#         break
#     print(valor)

# Gestor de contexto usando un generador
@contextmanager
def abrir_archivo(path: str, modo: str):
    """Gestiona la apertura y cierre de un archivo de forma segura."""
    f = open(path, modo, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

# Ejemplo de uso del gestor de contexto personalizado
# with abrir_archivo('ejemplo.txt', 'w') as archivo:
#     archivo.write('Hola, mundo')

