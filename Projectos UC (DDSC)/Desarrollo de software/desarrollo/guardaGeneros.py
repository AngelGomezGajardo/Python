
def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas

archivo=leer_archivo()

auxgeneros_peliculas=list()
generos_peliculas=tuple()
Coma=list()
generos=list()
for itera in archivo:
    Coma=itera.split(",")
    generos.append(Coma[4])
for genero in generos:
    separado=genero.split(";")
    for itera3 in separado:
        if itera3 not in auxgeneros_peliculas:
            auxgeneros_peliculas.append(itera3)
generos_peliculas=tuple(auxgeneros_peliculas)

for genero in generos_peliculas:
    print(f"    - {genero}")
