##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, tiempo_entrega):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75, 100)

    def repartir(self, pedido):
        # print(pedido)
        largo = ((len(pedido)))
        # print(largo)
        # print(f"energia al inicio {self.energia}")
        # print(f"Tiempo entrega libre {self.tiempo_entrega}")
        # calculo de gasto energia
        tiempo_demora_pedido = 0
        if largo <= 2 and self.energia >= 5:
            self.energia -= 5
            tiempo_demora_pedido = self.tiempo_entrega * 1.25
            # print(f"el pedido es de 2 o menos platos, por lo tanto, se descuentan 5, \nla energia total es:{self.energia}")
            # print(f"el tiempo de entrega 2 o menos platos es de {self.tiempo_entrega}")
        elif largo >= 3 and self.energia >= 15:
            self.energia -= 15
            tiempo_demora_pedido = self.tiempo_entrega * 0.85
            # print(f"el pedido es de 3 o mas platos, por lo tanto, se descuentan 15, \nla energia total es:{self.energia}")
            # print(f"el tiempo de entrega para 3 o mas platos es de {self.tiempo_entrega}")
        else:
            print("repartidor sin energia suficiente para el pedido")
            tiempo_demora_pedido = None
        return tiempo_demora_pedido


### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)

    def cocinar(self, informacion_plato):
        # informacion_plato: ["nombre", "tipo"]

        if informacion_plato[1] == "Bebestible":
            plato = Bebestible(informacion_plato[0])  # creamos la instancia
            # comparamos para asignar energia
            if plato.tamano == "pequeño":
                self.energia -= 5
            elif plato.tamano == "mediano":
                self.energia -= 8
            elif plato.tamano == "grande":
                self.energia -= 10

        elif informacion_plato[1] == "Comestible":
            plato = Comestible(informacion_plato[0])
            self.energia -= 15

        else:
            print("Tipo de plato no válido: usa 'Bebestible' o 'Comestible'.")

        if plato.dificultad > self.habilidad:
            plato.calidad *= 0.7
        else:
            plato.calidad *= 1.5

        return plato


### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        cantidad_platos = len(platos_preferidos)
        if cantidad_platos >= 1 and cantidad_platos <= 5:
            # print("cantidad platos:",cantidad_platos)
            self.platos_preferidos = platos_preferidos
        else:
            print("fuera de rango para platos preferidos")
            platos_preferidos = []
            self.platos_preferidos = platos_preferidos

    def recibir_pedido(self, pedido, demora):
        calificacion = 10
        self.pedido = pedido
        self.demora = demora
        # print(f"cantidad de platos en pedido: {len(self.pedido)}")
        # print(f"cantidad de platos preferidos: {len(self.platos_preferidos)}")
        if (len(self.pedido)) < (len(self.platos_preferidos)) or self.demora >= 20:
            # print("calificacion cambia")
            calificación = calificacion / 2
            for i in range(len(self.pedido)):
                plato = self.pedido[i]
                if (plato.calidad) >= 11:
                    calificacion += 11
                elif (plato.calidad) <= 8:
                    calificacion -= 3
            if calificacion < 0:
                calificacion = 0
        else:
            print("calificacion se mantiene")
            calificacion = calificacion

        return calificacion


### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = [
        "Jugo Natural",
        "Empanadas",
        ]
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos:
            print(f" - {plato}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
