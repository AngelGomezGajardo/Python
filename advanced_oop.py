"""
Programación orientada a objetos y metaprogramación básica en Python.

Este módulo cubre:

- Definición de clases y herencia para reutilizar código.
- Métodos especiales (mágicos) como `__repr__` y `__add__` que permiten personalizar el comportamiento de los objetos.
- Métodos de clase y estáticos para operaciones asociadas a la clase en lugar de instancias.
- Uso de `@dataclass` para generar clases inmutables o de datos con menos código repetitivo.
"""

# Definición de clases y herencia

class Animal:
    """Clase base para animales."""
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def hablar(self) -> str:
        """Método a sobrescribir por las subclases."""
        raise NotImplementedError("Este método debe ser implementado en las subclases")

class Perro(Animal):
    def hablar(self) -> str:
        return "Guau"

class Gato(Animal):
    def hablar(self) -> str:
        return "Miau"

# Métodos mágicos y sobrecarga de operadores
class Vector:
    """Representa un vector bidimensional y admite suma mediante el operador +."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

# Ejemplo de uso de métodos mágicos
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Utiliza __add__
print(v3)

# Métodos de clase y estáticos
class Contador:
    """Ejemplo de contador que rastrea cuántas instancias se han creado."""
    _cuenta = 0

    def __init__(self) -> None:
        Contador._cuenta += 1

    @classmethod
    def cantidad_instancias(cls) -> int:
        """Devuelve cuántas instancias de Contador se han creado."""
        return cls._cuenta

    @staticmethod
    def descripcion() -> str:
        return "Esta clase cuenta cuántas veces ha sido instanciada."

c1 = Contador()
c2 = Contador()
print(Contador.cantidad_instancias())  # 2
print(Contador.descripcion())

# Uso de dataclasses para definir clases de datos de forma concisa
from dataclasses import dataclass

@dataclass
class Punto:
    x: float
    y: float

# Crear instancias de Punto
p1 = Punto(1.0, 2.0)
p2 = Punto(3.0, 4.0)
print(p1)
print(p2)

