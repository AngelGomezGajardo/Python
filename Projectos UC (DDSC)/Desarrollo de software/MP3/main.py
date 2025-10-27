##############################################################
from random import seed, randint
import personas, platos, restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###
def crear_repartidores():
    r1 = personas.Repartidor("Tomás", randint(20, 30))
    r2 = personas.Repartidor("Daniela", randint(20, 30))
    lista_repartidores=[r1, r2]
    return lista_repartidores

def crear_cocineros():
    c1 = personas.Cocinero("Raúl", randint(1, 10))
    c2 = personas.Cocinero("Camila", randint(1, 10))
    c3 = personas.Cocinero("Matías", randint(1, 10))
    c4 = personas.Cocinero("Sofía", randint(1, 10))
    c5 = personas.Cocinero("Pedro", randint(1, 10))
    lista_cocineros=[c1,c2,c3,c4,c5]
    return lista_cocineros

def crear_clientes():
    cl1 = personas.Cliente("Javiera",   ["Pepsi",       "Empanadas"])
    cl2 = personas.Cliente("Ignacio",   ["Jugo Natural","Mariscos"])
    cl3 = personas.Cliente("Valentina", ["Agua",        "Papas Duqueza"])
    cl4 = personas.Cliente("Felipe",    ["Coca-Cola",   "Lomo a lo Pobre"])
    cl5 = personas.Cliente("Constanza", ["Pepsi",       "Empanadas"])
    lista_clientes=[cl1, cl2, cl3, cl4, cl5]
    return lista_clientes

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    rest_Goemon = restaurante.Restaurante("Goemon", INFO_PLATOS, cocineros, repartidores)
    return rest_Goemon

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Juan", "Jorge", "Pablo", "Luis", "Sofia", "Macarena"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("DSP")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
