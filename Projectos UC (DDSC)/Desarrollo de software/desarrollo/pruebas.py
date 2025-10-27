def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas

criterio="cantidad de votos"
genero_pelicula="Music"


archivo=leer_archivo()
resultados=[]
if criterio == "cantidad de votos":
    lista_generos = []
    votoPromedio = []
    CantidadDeVotos=[]
    for lee in archivo:
        elemento = lee.split(",")
        popularidad = elemento[1]
        votoProm=elemento[2]
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

    print(resultados[0])
    print(resultados[1])
    print(resultados[2])