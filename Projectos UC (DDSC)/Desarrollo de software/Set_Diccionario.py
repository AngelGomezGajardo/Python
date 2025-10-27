#me llamo la atencion que son los datos de tipo hashables

# Tipos hashables
print(hash(10))         # int
print(hash("hola"))     # str
print(hash((1, 2, 3)))  # tuple inmutable

# Usar como clave en un diccionario
d = { (1, 2): "valor", "clave": 123 }
print(d[(1, 2)])  # funciona

# Tipos NO hashables
try:
    hash([1, 2, 3])  # list
except TypeError as e:
    print(e)  # unhashable type: 'list'

try:
    s = set()
    s.add([1, 2, 3])  # error porque list no es hashable
except TypeError as e:
    print(e)