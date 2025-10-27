##############################################################
import personas
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0
        # print(f"Nombre Restaurant: {self.nombre}\nplatos: {self.platos}\ncocineros: {self.cocineros}\n repartidores: {self.repartidores} \ncalificacion: {self.calificacion}")

    # obtengo los platos preferidos por cada cliente:

    def recibir_pedidos(self, clientes):
        self.clientes = clientes
        cant_cliente = len(self.clientes)
        print(f"cantidad clientes {cant_cliente}")
        suma = 0
        # obtenemos dentro del metodo los platos preferidos por cada cliente
        for i in range(len(self.clientes)):
            # obtenemos el o los platos preferidos del cliente
            preferidos = self.clientes[i].platos_preferidos
            pedido = []
            Cocinado = False

            # por cada plato preferido, buscamos un cocinero que lo cocine
            for j in range(len(preferidos)):
                PlatoAcocinar = preferidos[j]
                for k in range(len(self.cocineros)):
                    if self.cocineros[k].energia > 0:
                        # el primer cocinero con energia positiva
                        # print(f"primero cocinero con energia: {self.cocineros[k].nombre}")
                        # lo mandamos a cocinar el plato iterado antes
                        cocinado = self.cocineros[k].cocinar(self.platos[PlatoAcocinar])
                        print("cocinado")
                        Cocinado = True
                        pedido.append(cocinado)
                        break
                    else:
                        print("no cocinado, cocineros sin energia")
                        Cocinado = False
                        continue
            # buscamos un repartidor
            demora = 0
            repartido = False
            if len(pedido) > 0:
                # print(f"si el pedido contiene piezas, n {len(pedido)}")
                for l in range(len(self.repartidores)):
                    if self.repartidores[l].energia > 0:
                        demora = self.repartidores[l].repartir(pedido)
                        print(demora)
                        if demora > 0:
                            repartido = True
                            break
                if repartido == False:
                    print("no hay repartidores disponibles")
                    pedido = []
                    demora = 0
            else:
                pedido = []
                demora = 0
        # calculamos calificacion
        numero = self.clientes[i].recibir_pedido(pedido, demora)
        suma += numero

        if cant_cliente > 0:
            self.calificacion = suma / cant_cliente
        else:
            self.calificacion = 0
        print(f"calificacion del restaurant {self.calificacion}")



### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")

#Test metodo
#cl1 = personas.Cliente("Javiera",   ["Pepsi",       "Empanadas"])
#cl2 = personas.Cliente("Ignacio",   ["Jugo Natural","Mariscos"])
#cl3 = personas.Cliente("Pedro",   ["Jugo Natural","Mariscos"])
#listClientes=[cl1,cl2,cl3]
#
#un_restaurante.recibir_pedidos(listClientes)