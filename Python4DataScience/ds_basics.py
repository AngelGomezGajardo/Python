"""
Introducción a Python para Ciencia de Datos.

Este módulo muestra tres niveles para cargar y explorar datos:

1. **Nivel básico:** Uso del módulo `csv` de la biblioteca estándar para leer un archivo CSV y almacenar las filas en listas de diccionarios.
2. **Nivel intermedio:** Uso de `pandas` para cargar un `DataFrame`, seleccionar columnas y calcular estadísticas simples.
3. **Nivel pro:** Uso de `pandas` con especificación explícita de tipos de datos para optimizar memoria y ejemplos de filtrado/slicing avanzado.

Todos los ejemplos están comentados en español para su comprensión didáctica.
"""

import csv
from pprint import pprint

# Ruta al conjunto de datos de ejemplo
datos_csv = "dataset.csv"

# Nivel básico: leer CSV con el módulo estándar
# -------------------------------------------------

with open(datos_csv, newline='', encoding='utf-8') as csvfile:
    lector = csv.DictReader(csvfile)
    filas = list(lector)

print("Nivel básico: primer registro cargado con csv.DictReader")
pprint(filas[0])

# Nivel intermedio: usar pandas para cargar y explorar datos
# ---------------------------------------------------------

try:
    import pandas as pd
except ImportError:
    raise SystemExit("Pandas no está instalado. Ejecute 'pip install pandas' para utilizar este ejemplo intermedio.")

# Cargar todo el CSV como DataFrame
df = pd.read_csv(datos_csv)
print("\nNivel intermedio: dimensiones del DataFrame (filas, columnas)")
print(df.shape)
print("\nResumen estadístico de columnas numéricas")
print(df.describe())

# Nivel pro: especificar tipos de datos y filtrado avanzado
# ---------------------------------------------------------

# Especificamos tipos de datos para reducir uso de memoria
column_types = {
    'id': 'int32',
    'edad': 'int8',
    'salario': 'int32',
    'compras': 'int8',
    'categoria': 'category'
}
df_opt = pd.read_csv(datos_csv, dtype=column_types)
print("\nNivel pro: tipos de datos optimizados")
print(df_opt.dtypes)

# Filtrado avanzado: seleccionar empleados con salario > 50.000 y que hayan realizado compras
condicion = (df_opt['salario'] > 50000) & (df_opt['compras'] == 1)
subset = df_opt.loc[condicion, ['id', 'edad', 'salario', 'categoria']]
print("\nNivel pro: registros con salario > 50.000 y compras realizadas")
print(subset)
