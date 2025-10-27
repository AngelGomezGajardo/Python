#     obtener_puntaje_y_votos(nombre_pelicula): Esta función recibe un          #
#     string, que corresponde al nombre de una película y debe retornar una     #
#     tupla, donde el primer elemento debe ser el puntaje promedio de la        #
#     película y el segundo elemento debe ser la cantidad de votos que tiene.   #

def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas
#leo la info
def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre
texto=leer_archivo()


nombre_pelicula="Star Wars: The Last Jedi"
# Cargar las lineas con la data del archivo
lineas_archivo = leer_archivo()
# Completar con lo que falta aquí
for itera in lineas_archivo:
    elemento = itera.split(",")
    titulo = elemento[0]
    voto_promedio = elemento[2]
    cantidad_votos = elemento[3]
    if titulo==nombre_pelicula:
        print("encontrado el titulo")


#American Sniper