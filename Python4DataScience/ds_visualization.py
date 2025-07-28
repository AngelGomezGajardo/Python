"""
Visualización de datos con múltiples herramientas.

1. **Nivel básico:** Uso de `matplotlib.pyplot` para crear gráficos simples (líneas y barras).
2. **Nivel intermedio:** Uso de `seaborn` para realizar visualizaciones estadísticas con menos código y estética mejorada.
3. **Nivel pro:** Personalización avanzada de gráficos (estilos, subplots) y breve mención a bibliotecas interactivas como Plotly.

Las visualizaciones no se ejecutan automáticamente en este contexto; utilice un entorno local para generar las figuras.
"""

# Nivel básico: matplotlib
# ------------------------

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.arange(0, 10, 1)
y = x ** 2

# Gráfico de líneas básico
plt.figure()
plt.plot(x, y, marker='o')
plt.title('Gráfico de líneas básico')
plt.xlabel('X')
plt.ylabel('Y = X^2')
# plt.show()  # Descomentar para visualizar

# Gráfico de barras básico
categorias = ['A', 'B', 'C']
valores = [10, 24, 7]

plt.figure()
plt.bar(categorias, valores)
plt.title('Gráfico de barras básico')
plt.xlabel('Categoría')
plt.ylabel('Valor')
# plt.show()

# Nivel intermedio: seaborn
# ------------------------

try:
    import seaborn as sns
except ImportError:
    raise SystemExit("Seaborn no está instalado. Ejecute 'pip install seaborn' para utilizar este ejemplo intermedio.")

# DataFrame a partir de un diccionario para gráficos
import pandas as pd
data = pd.DataFrame({
    'categoria': categorias,
    'valor': valores
})

plt.figure()
sns.barplot(data=data, x='categoria', y='valor')
plt.title('Gráfico de barras con seaborn')
# plt.show()

# Nivel pro: personalización avanzada y librerías interactivas
# -----------------------------------------------------------

# Subgráficos personalizados con matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, y, color='green', linestyle='--')
axes[0].set_title('Línea personalizada')
axes[1].bar(categorias, valores, color='orange')
axes[1].set_title('Barra personalizada')
# plt.show()

# Nota: Para visualizaciones interactivas, considere usar la biblioteca Plotly:
# import plotly.express as px
# fig = px.scatter(data_frame=df, x='edad', y='salario', color='categoria')
# fig.show()
