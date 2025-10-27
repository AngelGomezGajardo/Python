def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas

archivo=leer_archivo()

generos=list()
peliculas=list()
separado=list()
for itera in archivo:
    elemento=itera.split(",")
    titulo=elemento[0]
    popularidad=elemento[1]
    voto_promedio=elemento[2]
    cantidad_votos=elemento[3]

    separado = elemento[4].split(";")
    generos=[]
    for genero in separado:
        generos.append(genero)
    peliculas.append((titulo, popularidad, voto_promedio,cantidad_votos,generos))
print(peliculas)
info_peliculas=tuple()
info_peliculas=tuple(peliculas)

