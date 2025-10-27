from warnings import catch_warnings

import mysql.connector as db
#creacion de conexion
conn = db.connect(
    host="localhost",
    user="root",
    password="123456",
    database="mp1"
)
print("conexiones exitosa")
print("")
#Primera Consulta
print("Consulta 1 \n")
cursor=conn.cursor()
consulta1="""SELECT * FROM sociedades 
            WHERE rut="77886308-1" """
cursor.execute(consulta1)
filas=cursor.fetchall()
for fila in filas:
    print(fila)
print("")
print("Consulta 2 \n")
#Segunda Consulta
consulta2=""" SELECT * FROM sociedades 
                WHERE nombre LIKE 'Agencia%';
"""

cursor.execute(consulta2)
filas2=cursor.fetchall()

for fila2 in filas2:
    print(fila2)
print("")
print("Consulta 3 \n")
consulta3=""" SELECT * FROM sociedades 
                WHERE capital>=400000000;;
            """
cursor.execute(consulta3)
filas3=cursor.fetchall()

for fila3 in filas3:
    print(fila3)
print("")

print("")
print("Insertar datos 1 \n")
insertar = """INSERT INTO  sociedades 
        (id, rut, nombre, registro, comuna, capital) 
        VALUES(5156305, "77721389-K", "Estrellas SpA", "2024-03-11" , "PROVIDENCIA" ,1000000);
"""
try:
    cursor.execute(insertar)
    conn.commit()
    print("Insertar datos ejecutado correctamente")
except db.Error as e:
    print("Error al insertar datos:", e)


conn.close()
