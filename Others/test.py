import numpy as np


def rot_z(degrees):
    """Crea una matriz de rotación 3x3 alrededor del eje Z."""
    radians = np.radians(degrees)
    cos_theta, sin_theta = np.cos(radians), np.sin(radians)
    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])


def create_transformation_matrix(x, y, z, a, b, c):
    """Crea una matriz de transformación homogénea 4x4 a partir de un FRAME."""
    R = rot_z(c)  # Solo considerando rotación en Z para este ejemplo
    P = np.array([[x], [y], [z]])  # Vector de traslación

    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = P.flatten()

    return T


def apply_operator(A, B):
    """Simula el operador `:` en KRL combinando dos matrices de transformación."""
    return np.dot(A, B)


def extract_euler_angles(R):
    """Extrae los ángulos de Euler (A, B, C) de una matriz de rotación 3x3."""
    B = np.arctan2(-R[2, 0], np.sqrt(R[0, 0] ** 2 + R[1, 0] ** 2))
    if np.abs(B - np.pi / 2) < 1e-6:
        A = 0
        C = np.arctan2(R[0, 1], R[1, 1])
    elif np.abs(B + np.pi / 2) < 1e-6:
        A = 0
        C = -np.arctan2(R[0, 1], R[1, 1])
    else:
        A = np.arctan2(R[1, 0] / np.cos(B), R[0, 0] / np.cos(B))
        C = np.arctan2(R[2, 1] / np.cos(B), R[2, 2] / np.cos(B))
    return np.degrees(A), np.degrees(B), np.degrees(C)


# Definir valores iniciales
FRAME_ACTUAL = create_transformation_matrix(-104.17, 279.84, 344.04, -105, 0.0, 90)

# Desplazamiento en Z en el sistema del robot
DESPLAZAMIENTO_LOCAL = np.array([[0], [0], [-75], [1]])

# Aplicar la transformación de orientación al desplazamiento
DESPLAZAMIENTO_GLOBAL = np.dot(FRAME_ACTUAL, DESPLAZAMIENTO_LOCAL)

# Crear matriz de desplazamiento global
DESPLAZAMIENTO = create_transformation_matrix(DESPLAZAMIENTO_GLOBAL[0, 0], DESPLAZAMIENTO_GLOBAL[1, 0],
                                              DESPLAZAMIENTO_GLOBAL[2, 0], 0.0, 0.0, 0.0)

# Aplicar la transformación (equivalente a operador `:` en KRL)
FRAME_RESULTANTE = apply_operator(FRAME_ACTUAL, DESPLAZAMIENTO)

# Mostrar resultado
print("\nMatriz de transformación resultante:")
print(FRAME_RESULTANTE)

# Extraer posición resultante
pos_resultante = FRAME_RESULTANTE[:3, 3]
print("\nPosición resultante (X, Y, Z):")
print(pos_resultante)

# Extraer ángulos de Euler resultantes
R_resultante = FRAME_RESULTANTE[:3, :3]
a_resultante, b_resultante, c_resultante = extract_euler_angles(R_resultante)
print("\nÁngulos resultantes (A, B, C en grados):")
print(f"A: {a_resultante:.2f}, B: {b_resultante:.2f}, C: {c_resultante:.2f}")
