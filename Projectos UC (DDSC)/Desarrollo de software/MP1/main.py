# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    ##################################################
    # Generos Peliculas
    archivo = lineas_archivo

    auxgeneros_peliculas = list()
    generos_peliculas = tuple()
    Coma = list()
    generos = list()
    for itera in archivo:
        Coma = itera.split(",")
        generos.append(Coma[4])
    for genero in generos:
        separado = genero.split(";")
        for itera3 in separado:
            if itera3 not in auxgeneros_peliculas:
                auxgeneros_peliculas.append(itera3)
    generos_peliculas = tuple(auxgeneros_peliculas)
    ##################################################
    # Peliculas por genero
    generos_peliculas = list()

    lista_generos = []
    peliculas_por_genero = []
    for lee in archivo:
        elemento = lee.split(",")
        generos = elemento[4].split(";")
        for genero in generos:
            if genero not in lista_generos:
                lista_generos.append(genero)

    # valido lista de generos
    # for i in lista_generos:
    #    print(i)
    for genero in lista_generos:
        lista_peliculas = []
        for lee in archivo:
            elemento = lee.split(",")
            titulo = elemento[0]
            generos_pelicula = elemento[4].split(";")
            if genero in generos_pelicula:
                lista_peliculas.append(titulo)
        peliculas_por_genero.append((genero, lista_peliculas))
    # valido



    ##################################################
    # info_peliculas

    generos = list()
    peliculas = list()
    separado = list()
    for itera in archivo:
        elemento = itera.split(",")
        titulo = elemento[0]
        popularidad = elemento[1]
        voto_promedio = elemento[2]
        cantidad_votos = elemento[3]

        separado = elemento[4].split(";")
        generos = []
        for genero in separado:
            generos.append(genero)
        peliculas.append((titulo, popularidad, voto_promedio, cantidad_votos, generos))

    info_peliculas = tuple()
    info_peliculas = tuple(peliculas)
    ##################################################
    # devolver como tuplas las 3 infos
    return generos_peliculas, peliculas_por_genero, info_peliculas
    pass



# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    lineas_archivo = leer_archivo()
    punto_y_votos = []
    cantidad_votos=[]
    voto_promedio=[]
    nombre_pelicula.strip().rstrip()
    nombre_pelicula.lower()
    for itera in lineas_archivo:
        elemento = itera.split(",")
        titulo = elemento[0]
        titulo.strip().rstrip()
        titulo.lower()
        voto_promedio = elemento[2]
        cantidad_votos = elemento[3]
        if titulo == nombre_pelicula:
            punto_y_votos.append((titulo, voto_promedio, cantidad_votos))
            break
        else:
            voto_promedio=[]
            cantidad_votos=[]
    return voto_promedio, cantidad_votos
    pass


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    archivo = leer_archivo()
    lista_generos = []
    for lee in archivo:
        elemento = lee.split(",")

        generos = elemento[4].split(";")
        for genero in generos:
            if genero not in lista_generos:
                lista_generos.append(genero)

    for genero in lista_generos:
        lista_peliculas = []
        for lee in archivo:
            elemento = lee.split(",")
            titulo = elemento[0]
            generos_pelicula = elemento[4].split(";")
            if genero_pelicula in generos_pelicula:
                lista_peliculas.append(titulo)
        lista_peliculas.sort(reverse=True)
    return lista_peliculas
    pass


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    generos_peliculas = list()
    archivo = leer_archivo()
    valorGuardadoMxm=0.0
    valorGuardadoMin=0.0
    promedio=0.0
    resultados = []

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
        # print(f"si imprime: {popularidadPelis}")

        # buscamos el valor de popularidad MAXIMO
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

        # calculamos el valor PROMEDIO de popularidad
        suma = 0
        rango = (len(popularidadPelis))
        for i in range(len(popularidadPelis)):
            numero = float(popularidadPelis[i])
            suma = numero + suma
        # print(f"esta es la suma {suma}")
        promedio = suma / rango
        #print(f"Promedio {promedio}")


    ################################################################################################################
    ################################################################################################################


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
        #print(f"Promedio {promedio}")


    ################################################################################################################
    ################################################################################################################

    if criterio == "cantidad de votos":
        #print("entramos a cantida de votos")
        lista_generos = []
        Votos = []
        for lee in archivo:
            elemento = lee.split(",")
            CantVotos = elemento[3]
            generos = elemento[4].split(";")

            for genero in generos:
                if genero not in lista_generos:
                    lista_generos.append(genero)

            for genero in generos:
                if genero == genero_pelicula:
                    #print("si se mete aqui")
                    Votos.append(CantVotos)
        #print("imprime cantidad de votos ",Votos)

        # buscamos el valor de popularidad MAXIMO
        valorGuardadoMxm = float(Votos[0])
        for i in Votos[1:]:
            numero = float(i)
            if numero > valorGuardadoMxm:
                valorGuardadoMxm = numero

        # buscamos el valor de popularidad MINIMO
        valorGuardadoMin = float(Votos[0])
        for i in Votos[1:]:
            numero = float(i)
            if numero < valorGuardadoMin:
                valorGuardadoMin = numero

        # calculamos el valor PROMEDIO de popularidad
        suma = 0
        rango = (len(Votos))
        for i in range(len(Votos)):
            numero = float(Votos[i])
            suma = numero + suma
        promedio = suma / rango
    #print(promedio)
    # guardamos los valores en la lista
    resultados.append(valorGuardadoMxm)
    resultados.append(valorGuardadoMin)
    resultados.append(promedio)
    pass
    return resultados[0], resultados[1], resultados[2]

# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
