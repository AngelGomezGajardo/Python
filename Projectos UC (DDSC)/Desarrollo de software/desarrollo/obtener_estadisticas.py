def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    #print("archivo leido")
    return lineas_peliculas
#   (genero_pelicula, criterio): Esta función recibe
#   un string que corresponde a un género de película. Debes analizar las
#   películas que sean de este género y obtener el máximo, mínimo y
#   promedio de los valores dados por criterio (que puede ser “popularidad”,
#   “voto promedio”, “cantidad votos”). Esto debe ser entregado en formato de
#   lista con el formato [max, min, promedio], en el orden mostrado.

def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    generos_peliculas = list()
    archivo=leer_archivo()
    resultados=[]
    promedio=0.0

    if criterio == "popularidad":

        lista_generos = []
        popularidadPelis = []
        for lee in archivo:
            elemento = lee.split(",")
            popularidad = elemento[1]
            generos = elemento[4].split(";")

            for genero in generos:
                if genero not in lista_generos:
                    lista_generos.append(genero)

            for genero in generos:
                if genero == genero_pelicula:
                    popularidadPelis.append(popularidad)
        #print(f"si imprime: {popularidadPelis}")

        #buscamos el valor de popularidad MAXIMO
        valorGuardadoMxm = float(popularidadPelis[0])
        for i in popularidadPelis[1:]:
            numero = float(i)
            if numero > valorGuardadoMxm:
                valorGuardadoMxm = numero

        # buscamos el valor de popularidad MINIMO
        valorGuardadoMin = float(popularidadPelis[0])
        for i in popularidadPelis[1:]:
            numero = float(i)
            if numero < valorGuardadoMin:
                valorGuardadoMin = numero

        #calculamos el valor PROMEDIO de popularidad
        suma = 0
        rango = (len(popularidadPelis))
        for i in range(len(popularidadPelis)):
            numero = float(popularidadPelis[i])
            suma = numero + suma
        #print(f"esta es la suma {suma}")
        promedio = suma / rango
        #print(f"Promedio {promedio}")


        resultados.append(valorGuardadoMxm)
        resultados.append(valorGuardadoMin)
        resultados.append( promedio)
        #print("ESTO LO IMPRIME?",resultados[0])
        #print(resultados[1])
        #print(resultados[2])
    ################################################################################################################
    #reservado para los otros valores a calcular
    votoPromedio = []
    archivo = leer_archivo()
    resultados = []

    if criterio == "voto promedio":
        lista_generos = []
        votoPromedio = []
        for lee in archivo:
            elemento = lee.split(",")
            popularidad = elemento[1]
            votoProm = elemento[2]
            generos = elemento[4].split(";")

            for genero in generos:
                if genero not in lista_generos:
                    lista_generos.append(genero)

            for genero in generos:
                if genero == genero_pelicula:
                    votoPromedio.append(votoProm)
        # print(f"si imprime: {popularidadPelis}")

        # buscamos el valor de popularidad MAXIMO
        valorGuardadoMxm = float(votoPromedio[0])
        for i in votoPromedio[1:]:
            numero = float(i)
            if numero > valorGuardadoMxm:
                valorGuardadoMxm = numero

        # buscamos el valor de popularidad MINIMO
        valorGuardadoMin = float(votoPromedio[0])
        for i in votoPromedio[1:]:
            numero = float(i)
            if numero < valorGuardadoMin:
                valorGuardadoMin = numero

        # calculamos el valor PROMEDIO de popularidad
        suma = 0
        rango = (len(votoPromedio))
        for i in range(len(votoPromedio)):
            numero = float(votoPromedio[i])
            suma = numero + suma
        # print(f"esta es la suma {suma}")
        promedio = suma / rango
        # print(f"Promedio {promedio}")

        resultados.append(valorGuardadoMxm)
        resultados.append(valorGuardadoMin)
        resultados.append(promedio)

        #print(resultados[0])
        #print(resultados[1])
        #print(resultados[2])


        archivo = leer_archivo()
        resultados = []
    if criterio == "cantidad de votos":
        lista_generos = []
        votoPromedio = []
        CantidadDeVotos = []
        for lee in archivo:
            elemento = lee.split(",")
            popularidad = elemento[1]
            votoProm = elemento[2]
            CantVotos = elemento[3]
            generos = elemento[4].split(";")

            for genero in generos:
                if genero not in lista_generos:
                    lista_generos.append(genero)

            for genero in generos:
                if genero == genero_pelicula:
                    CantidadDeVotos.append(CantVotos)
        # print(f"si imprime: {popularidadPelis}")

        # buscamos el valor de popularidad MAXIMO
        valorGuardadoMxm = float(CantidadDeVotos[0])
        for i in CantidadDeVotos[1:]:
            numero = float(i)
            if numero > valorGuardadoMxm:
                valorGuardadoMxm = numero

        # buscamos el valor de popularidad MINIMO
        valorGuardadoMin = float(CantidadDeVotos[0])
        for i in CantidadDeVotos[1:]:
            numero = float(i)
            if numero < valorGuardadoMin:
                valorGuardadoMin = numero

        # calculamos el valor PROMEDIO de popularidad
        suma = 0
        rango = (len(CantidadDeVotos))
        for i in range(len(CantidadDeVotos)):
            numero = float(CantidadDeVotos[i])
            suma = numero + suma
        # print(f"esta es la suma {suma}")
        promedio = suma / rango
        # print(f"Promedio {promedio}")

        resultados.append(valorGuardadoMxm)
        resultados.append(valorGuardadoMin)
        resultados.append(promedio)
        #validamos info
        #print(resultados[0])
        #print(resultados[1])
        #print(resultados[2])
    pass
    return resultados[0],resultados[1],resultados[2]

genero, criterio = solicitar_genero_y_criterio()
estadisticas = obtener_estadisticas(genero, criterio)
print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
print(f"    - Máximo: {estadisticas[0]}")
print(f"    - Mínimo: {estadisticas[1]}")
print(f"    - Promedio: {estadisticas[2]}")

