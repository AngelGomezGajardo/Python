# Importar liibrerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.
import mysql.connector as db
import csv

# Desde este punto en adelante se debe crear el código solicitado.

# Conexión a la base de datos
conn = db.connect(
  host="localhost",
  user="root",
  password="123456", # Cambiar por la contraseña de su base de datos
  database="mp2"
)
cursor = conn.cursor()
### Parte 1: Crear tablas ###
# Borrar tablas si existen
# Recuerden que no se puede borrar una tabla que es referenciada por una llave foránea, por lo que
# se debe borrar primero la tabla que contiene la llave foránea
# NO ES SEGURO BORRAR LAS TABLAS ASI COMO ASI EN TRABAJOS REALES
# estaba evaluando que errores aparecen

#borrar_tabla_pedidos = "DROP TABLE IF EXISTS pedidos"
#cursor.execute(borrar_tabla_pedidos)
#
#borrar_tabla_productos = "DROP TABLE IF EXISTS productos"
#cursor.execute(borrar_tabla_productos)
#
#borrar_tabla_clientes = "DROP TABLE IF EXISTS clientes"
#cursor.execute(borrar_tabla_clientes)
#
#borrar_tabla_productos_pedidos = "DROP TABLE IF EXISTS productos_pedidos"
#cursor.execute(borrar_tabla_productos_pedidos)

####################################################################################
# Se debe definir la llave foránea que referencia a sucursales
# y crear la tabla empleados después de crear sucursales

#creacion tabla 1
crear_tabla_productos = """
CREATE TABLE IF NOT EXISTS productos(
id int PRIMARY KEY,
nombre VARCHAR(255),
descripcion VARCHAR(255),
precio int)
"""
cursor.execute(crear_tabla_productos)

#creacion tabla 2
crear_tabla_clientes = """
CREATE TABLE IF NOT EXISTS clientes(
id int PRIMARY KEY,
nombre VARCHAR(255),
email VARCHAR(255))
"""
cursor.execute(crear_tabla_clientes)

#creacion tabla 3
crear_tabla_pedidos = """
CREATE TABLE IF NOT EXISTS pedidos
(
id int PRIMARY KEY,
fecha DATE,
direccion VARCHAR(255),
id_cliente int,
detalle VARCHAR(255),
FOREIGN KEY (id_cliente) REFERENCES clientes(id)
)
"""
cursor.execute(crear_tabla_pedidos)

#creacion tabla 4
crear_tabla_productos_pedidos = """
CREATE TABLE IF NOT EXISTS productos_pedidos
(
id_producto int,
id_pedido int,
cantidad int,
PRiMARY KEY (id_producto, id_pedido ),

FOREIGN KEY (id_producto) REFERENCES productos(id),
FOREIGN KEY (id_pedido) REFERENCES pedidos (id)
)
"""
cursor.execute(crear_tabla_productos_pedidos)

###############################################################
#               CARGA DE DATOS DESDE .CSV
###############################################################

# ======================================
# Clientes
# ======================================

with open ('data/clientes.csv', 'r') as file:
    CSV_Reader = csv.reader(file, delimiter=',')
    next(CSV_Reader)
    filas = [] # Creamos una lista vacía para insertar todas las filas usando executemany
    for row in CSV_Reader:
        filas.append(row)
insert_clientes = "INSERT INTO clientes (id, nombre , email ) VALUES (%s, %s, %s)"
try:
    cursor.executemany(insert_clientes, filas)
    conn.commit()
    print("Insertar datos ejecutado correctamente")
except db.Error as e:
    print("Error al insertar datos:", e)


# ======================================
#  insertar pedidos
# ======================================
with open ('data/pedidos.csv', 'r') as file:
    CSV_Reader = csv.reader(file, delimiter=',')
    next(CSV_Reader)
    filas = [] # Creamos una lista vacía para insertar todas las filas usando executemany
    for row in CSV_Reader:
        filas.append(row)
insert_pedidos = "INSERT INTO pedidos (id, fecha , direccion, id_cliente, detalle ) VALUES (%s, %s, %s, %s, %s)"

try:
    cursor.executemany(insert_pedidos, filas)
    conn.commit()
    print("Insertar datos ejecutado correctamente")
except db.Error as e:
    print("Error al insertar datos:", e)

# ======================================
# insertar productos
# ======================================
with open ('data/productos.csv', 'r') as file:
    CSV_Reader = csv.reader(file, delimiter=',')
    next(CSV_Reader)
    filas = [] # Creamos una lista vacía para insertar todas las filas usando executemany
    for row in CSV_Reader:
        filas.append(row)
insert_productos = "INSERT INTO productos(id,nombre,descripcion,precio) VALUES (%s, %s, %s, %s)"
try:
    cursor.executemany(insert_productos, filas)
    conn.commit()
    print("Insertar datos ejecutado correctamente")
except db.Error as e:
    print("Error al insertar datos:", e)


# ======================================
# insertar productos_pedidos
# ======================================
with open ('data/productos_pedidos.csv', 'r') as file:
    CSV_Reader = csv.reader(file, delimiter=',')
    next(CSV_Reader)
    filas = [] # Creamos una lista vacía para insertar todas las filas usando executemany
    for row in CSV_Reader:
        filas.append(row)
insert_productos_pedidos = "INSERT INTO productos_pedidos(id_producto,id_pedido,cantidad) VALUES (%s, %s, %s)"
try:
    cursor.executemany(insert_productos_pedidos, filas)
    conn.commit()
    print("Insertar datos ejecutado correctamente")
except db.Error as e:
    print("Error al insertar datos:", e)





## NO OLVIDAR el commit cuando modificamos la info en las tablas ##
# Execute cursor
conn.commit()
