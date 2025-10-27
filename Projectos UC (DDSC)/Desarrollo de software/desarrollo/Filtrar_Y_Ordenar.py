def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas

#      filtrar_y_ordenar(genero_pelicula): Esta función recibe un string que
#      corresponde a un género de película. Debes filtrar todas las películas que
#      sean de este género y retornar sus nombres en una lista. Además, esta
#      lista debe estar ordenada según orden alfabético inverso (es decir,
#      películas con z primero y al final películas con a).

#lo mismo que guar peliculas por genero, pero deben estar ordenadas, ademas que el usuario elige el tipo de genero
#que debe leer
def filtrar_y_ordenar(genero_pelicula):
    archivo=leer_archivo()
    lista_generos=[]
    for lee in archivo:
        elemento = lee.split(",")

        generos = elemento[4].split(";")
        for genero in generos:
            if genero not in lista_generos:
                lista_generos.append(genero)

    for genero in lista_generos:
        lista_peliculas=[]
        for lee in archivo:
            elemento=lee.split(",")
            titulo=elemento[0]
            generos_pelicula=elemento[4].split(";")
            if genero_pelicula in generos_pelicula:
                lista_peliculas.append(titulo)
        lista_peliculas.sort(reverse=True)
    return lista_peliculas

def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero

genero = solicitar_genero()
nombres_peliculas = filtrar_y_ordenar(genero)
print(f"\nNombres de películas del género {genero} ordenados:")
for nombre in nombres_peliculas:
    print(f"    - {nombre}")
