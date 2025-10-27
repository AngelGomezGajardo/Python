
def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas

archivo=leer_archivo()
final=[]
lista_generos=[]
peliculas_por_genero = []
for lee in archivo:
    elemento = lee.split(",")
    titulo = elemento[0]
    popularidad = elemento[1]
    voto_promedio = elemento[2]
    cantidad_votos = elemento[3]
    generos = elemento[4].split(";")
    for genero in generos:
        if genero not in lista_generos:
            lista_generos.append(genero)

#valido lista de generos
#for i in lista_generos:
#    print(i)
for genero in lista_generos:
    lista_peliculas=[]
    for lee in archivo:
        elemento=lee.split(",")
        titulo=elemento[0]
        generos_pelicula=elemento[4].split(";")
        if genero in generos_pelicula:
            lista_peliculas.append(titulo)
    peliculas_por_genero.append((genero,lista_peliculas))
#valido
#for i in peliculas_por_genero:
#    print(i)

#print("\nTítulos de películas por genero:")
#for genero in peliculas_por_genero:
#    print(f"    genero: {genero[0]}")
#    for titulo in genero[1]:
#        print(f"        - {titulo}")
#


















