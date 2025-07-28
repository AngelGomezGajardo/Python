"""
Programación asincrónica con asyncio.

Este módulo demuestra:

- Cómo definir corutinas usando `async def` y suspender su ejecución con `await`.
- Creación y ejecución de varias tareas concurrentemente usando `asyncio.create_task` y `asyncio.gather`.
- Uso de `asyncio.run` para iniciar un bucle de eventos de manera sencilla.
"""

import asyncio

async def tarea_lenta(nombre: str, segundos: int) -> str:
    """Simula una tarea que tarda un número determinado de segundos."""
    print(f"Iniciando tarea {nombre}")
    await asyncio.sleep(segundos)
    print(f"Tarea {nombre} completada")
    return nombre

async def main() -> None:
    """Crea y ejecuta varias tareas de manera concurrente."""
    tareas = [
        asyncio.create_task(tarea_lenta("A", 2)),
        asyncio.create_task(tarea_lenta("B", 1)),
        asyncio.create_task(tarea_lenta("C", 3)),
    ]
    resultados = await asyncio.gather(*tareas)
    print(f"Resultados: {resultados}")

# Para ejecutar este módulo directamente, descomentar el siguiente bloque:
# if __name__ == "__main__":
#     asyncio.run(main())

