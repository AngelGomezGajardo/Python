"""
Limpieza de datos en múltiples niveles.

1. **Nivel básico:** Limpieza manual de una lista de registros simulando la eliminación de valores nulos.
2. **Nivel intermedio:** Uso de `pandas` para detectar valores faltantes, eliminar duplicados y rellenar valores nulos.
3. **Nivel pro:** Uso de `sklearn.impute.SimpleImputer` para imputar valores faltantes con estrategias estadísticas.

Este ejemplo utiliza un conjunto de datos sintético para ilustrar las técnicas.
"""

from typing import List, Dict

# Nivel básico: lista de diccionarios con valores faltantes representados por None
datos: List[Dict[str, object]] = [
    {"nombre": "Ana", "edad": 25, "salario": 45000},
    {"nombre": "Luis", "edad": None, "salario": 52000},
    {"nombre": "María", "edad": 30, "salario": None},
    {"nombre": "Carlos", "edad": 28, "salario": 52000},
    {"nombre": "Ana", "edad": 25, "salario": 45000},  # Registro duplicado
]

# Eliminamos registros duplicados manualmente usando un conjunto de tuplas
vistos = set()
datos_sin_duplicados = []
for registro in datos:
    identificador = tuple(registro.items())
    if identificador not in vistos:
        datos_sin_duplicados.append(registro)
        vistos.add(identificador)

# Eliminamos registros con campos nulos de forma manual
datos_limpios_basico = [r for r in datos_sin_duplicados if None not in r.values()]
print("Nivel básico: registros después de eliminar duplicados y nulos:")
print(datos_limpios_basico)

# Nivel intermedio: usando pandas para limpiar
# -------------------------------------------

try:
    import pandas as pd
except ImportError:
    raise SystemExit("Pandas no está instalado. Ejecute 'pip install pandas' para utilizar este ejemplo intermedio.")

import numpy as np

df = pd.DataFrame(datos)
print("\nNivel intermedio: DataFrame original con posibles nulos y duplicados:")
print(df)

# Eliminar duplicados
df_sin_dup = df.drop_duplicates()

# Rellenar valores nulos: rellenamos edad con la media y salario con la mediana
edad_media = df_sin_dup['edad'].mean()
salario_mediana = df_sin_dup['salario'].median()
df_intermedio = df_sin_dup.fillna({
    'edad': edad_media,
    'salario': salario_mediana
})
print("\nNivel intermedio: DataFrame después de tratar nulos y duplicados:")
print(df_intermedio)

# Nivel pro: imputación con sklearn
# --------------------------------

try:
    from sklearn.impute import SimpleImputer
except ImportError:
    raise SystemExit("scikit-learn no está instalado. Ejecute 'pip install scikit-learn' para utilizar este ejemplo pro.")

# Convertimos a matriz NumPy para imputar solo columnas numéricas
numericas = df_sin_dup[['edad', 'salario']].to_numpy()

# Imputador: reemplaza valores faltantes con la media de cada columna
imputador = SimpleImputer(strategy='mean')
imputadas = imputador.fit_transform(numericas)

# Creamos un nuevo DataFrame con valores imputados
df_pro = df_sin_dup.copy()
df_pro[['edad', 'salario']] = imputadas
print("\nNivel pro: DataFrame después de imputar valores faltantes con SimpleImputer:")
print(df_pro)
