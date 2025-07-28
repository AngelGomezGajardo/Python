"""
Aprendizaje automático básico a avanzado con Python y scikit-learn.

1. **Nivel básico:** Implementación manual de regresión lineal utilizando la fórmula de la ecuación normal.
2. **Nivel intermedio:** Uso de `scikit-learn` para ajustar un modelo de regresión lineal y evaluar su desempeño.
3. **Nivel pro:** Uso de `Pipeline` y `GridSearchCV` para ajustar modelos con validación cruzada y búsqueda de hiperparámetros.

Se utiliza un conjunto de datos sintético de ejemplo.
"""

import numpy as np

# Generamos datos sintéticos (X: característica, y: variable objetivo)
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Nivel básico: cálculo manual de los coeficientes de regresión lineal
# -------------------------------------------------------------------

# Añadimos una columna de unos para el término independiente
X_b = np.c_[np.ones((100, 1)), X]

# Cálculo de la ecuación normal: (X^T X)^{-1} X^T y
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print("Nivel básico: coeficientes calculados manualmente")
print(f"Intersección: {theta_best[0][0]:.2f}, Pendiente: {theta_best[1][0]:.2f}")

# Nivel intermedio: uso de scikit-learn
# -------------------------------------

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
except ImportError:
    raise SystemExit("scikit-learn no está instalado. Ejecute 'pip install scikit-learn' para utilizar este ejemplo.")

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones y evaluación
predicciones = modelo.predict(X_test)
mse = mean_squared_error(y_test, predicciones)
print("\nNivel intermedio: parámetros de scikit-learn")
print(f"Intersección: {modelo.intercept_[0]:.2f}, Pendiente: {modelo.coef_[0][0]:.2f}")
print(f"Error cuadrático medio en el conjunto de prueba: {mse:.2f}")

# Nivel pro: Pipeline y GridSearchCV
# ----------------------------------

try:
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import GridSearchCV
except ImportError:
    raise SystemExit("scikit-learn no está completamente instalado. Asegúrese de tener instaladas todas las dependencias.")

# Creamos un pipeline para aplicar escalado, generación de características polinomiales y regresión
pipe = Pipeline([
    ('poly_features', PolynomialFeatures(include_bias=False)),
    ('scaler', StandardScaler()),
    ('reg', LinearRegression())
])

# Definimos la rejilla de parámetros para buscar el grado óptimo del polinomio
param_grid = {
    'poly_features__degree': [1, 2, 3],
}

# Usamos validación cruzada para encontrar el mejor modelo
grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X, y.ravel())

print("\nNivel pro: mejores parámetros obtenidos con GridSearchCV")
print(grid_search.best_params_)
print(f"Mejor puntuación (negativa MSE): {grid_search.best_score_:.2f}")
