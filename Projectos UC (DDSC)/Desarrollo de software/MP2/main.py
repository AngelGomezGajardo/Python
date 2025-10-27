import parametros as p
import random

# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion, tipo):
        if accion == "acelerar":
            if tipo == "automovil":
                self.resistencia_actual -= 5
            elif tipo == "moto":
                self.resistencia_actual -= 3
        elif accion == "frenar":
            if tipo == "automovil":
                self.resistencia_actual -= 10
            elif tipo == "moto":
                self.resistencia_actual -= 7
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR
def seleccionar(vehiculos):
    if not len(vehiculos):
        print("No hay vehículos instanciados todavía")
        return

    print("Los vehículos disponibles son:")
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input("indica el numero del vehiculo a seleccionar: \n"))
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases
def avanzar(velocidad, tiempo):
    # Completar
    kilometraje = (velocidad * tiempo) / 1000
    return kilometraje


class Automovil:

    def __init__(self, kilometraje, ano):
        self.kilometraje = kilometraje  # kilometraje del vehiculo expresado en kilometros
        self.ano = ano
        self.ruedas = [Rueda() for _ in range(4)]  # igual que en ayudantia
        self.aceleracion = 0
        self.velocidad = 0

    def __str__(self):
        return f"Automovil con kilometraje de {self.kilometraje} km, y año {self.ano}"

    def avanzar(self, tiempo):
        velocidad_ms = self.velocidad / 3.6
        kmRecorridos = avanzar(velocidad_ms, tiempo)
        self.kilometraje += kmRecorridos

    def acelerar(self, tiempo_ss):
        tiempo_hh = tiempo_ss / 3600
        self.aceleracion += tiempo_hh * 0.5
        self.velocidad += self.aceleracion * tiempo_hh
        self.avanzar(tiempo_ss)
        for i in self.ruedas:  # igual a ejemploo ayudandtia
            i.gastar("acelerar", "automovil")
        self.aceleracion = 0

    def frenar(self, tiempo_ss):
        tiempo_hh = tiempo_ss / 3600
        self.aceleracion -= tiempo_hh * 0.5

        self.velocidad += self.aceleracion * tiempo_hh
        if self.velocidad < 0:
            self.velocidad = 0
        self.avanzar(tiempo_ss)
        for i in self.ruedas:  # igual a ejemploo ayudandtia
            i.gastar("frenar", "automovil")

        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_ruedas(self):
        baja_resistencia = self.ruedas[0]  # instancia de las ruedas, guarda la primera rueda
        indice=0
        for i in range(len(self.ruedas)):  # ok
            if self.ruedas[i].resistencia_actual < baja_resistencia.resistencia_actual:
                baja_resistencia = self.ruedas[i]  # guarda el valor mas bajo de resistencia
                indice = i  # guarda el indice que se encuentra el valor mas bajo de resistencia
        self.ruedas.pop(indice)  # eliminamos el indice que almacena el valor mas bajo
        self.rueda_nueva = Rueda()  # creamos una nueva instancia de rueda
        self.ruedas.insert(indice, self.rueda_nueva)  # agregamos una nueva rueda en la misma posicion


class Moto:
    def __init__(self, kilometraje, ano, cilindrada):
        self.kilometraje = kilometraje  # kilometraje del vehiculo expresado en kilometros
        self.ano = ano
        self.ruedas = [Rueda() for _ in range(2)]  # igual que en ayudantia
        self.aceleracion = 0
        self.velocidad = 0
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Moto con kilometraje de {self.kilometraje}, año {self.ano}, y cilindrada de {self.cilindrada} cc"

    def avanzar(self, tiempo):
        velocidad_ms = self.velocidad / 3.6
        kmRecorridos = avanzar(velocidad_ms, tiempo)
        self.kilometraje += kmRecorridos

    def acelerar(self, tiempo_ss):
        tiempo_hh = tiempo_ss / 3600
        self.aceleracion += (tiempo_hh * 0.8) + (self.cilindrada * 0.2)
        self.velocidad += self.aceleracion * tiempo_hh*3
        self.avanzar(tiempo_ss)
        for i in self.ruedas:  # igual a ejemploo ayudandtia
            i.gastar("acelerar", "moto")
        self.aceleracion = 0

    def frenar(self, tiempo_ss):
        tiempo_hh = tiempo_ss / 3600
        self.aceleracion -= (tiempo_hh * 0.8) + (self.cilindrada * 0.2)
        self.velocidad += self.aceleracion * tiempo_hh * 2
        if self.velocidad <=0 :
            self.velocidad=0
        self.avanzar(tiempo_ss)
        for i in self.ruedas:  # igual a ejemploo ayudandtia
            i.gastar("frenar", "moto")
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_ruedas(self):
        for i in range(len(self.ruedas)):  # ok
            if self.ruedas[i].resistencia_actual < self.ruedas[i].resistencia_total*0.5:
                self.ruedas.pop(i)  # eliminamos el indice que almacena el valor mas bajo
                self.ruedas.insert(i,Rueda() )  # agregamos una nueva rueda en la misma posicion
                #print(f"rueda reemplazada: {i+1}")#test cual rueda reemplaza


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        try:
            tiempo_acelerar=float(input("ingrese el tiempo a acelerar: "))
            vehiculo.acelerar(tiempo_acelerar)
            X=tiempo_acelerar
            Y=(vehiculo.velocidad)
            print(f"Se ha acelerado por {X} segundos, llegando a una velocidad de {Y} km/h")
        except ValueError:
            print("solo admite numeros")
    elif opcion == 3:  # Frenar
        try:
            tiempo_frenar=float(input("ingrese el tiempo a frenar: "))
            vehiculo.frenar(tiempo_frenar)
            X=tiempo_frenar
            Y=(vehiculo.velocidad)
            print(f"Se ha frenado {X} segundos, llegando a una velocidad de {Y} km/h")
        except ValueError:
            print("solo admite numeros")
    elif opcion == 4:  # Avanzar
        try:
            tiempo_avanzar=float(input("ingrese el tiempo a avanzar"))
            vehiculo.avanzar(tiempo_avanzar)
            X=tiempo_avanzar
            Y=(vehiculo.velocidad)
            print(f"se ha avanzado {X} segundos a una velocidad de {Y} km/h")
        except ValueError:
            print("solo se admiten numeros")
    elif opcion == 5:  # Cambiar rueda
        R_Reemplazada=False
        vehiculo.reemplazar_ruedas()
        for i in range(len(vehiculo.ruedas)):
           if vehiculo.ruedas[i].estado=="Perfecto":
                R_Reemplazada=True
        if R_Reemplazada==True:
            print("Se han reemplazado las ruedas con éxito")
        else:
            print("no es necesario reemplazar ruedas")
    elif opcion == 6:  # Mostrar Estado
        print(f"Año: {vehiculo.ano}")
        print(f"Velocidad: {vehiculo.velocidad}")
        print(f"kilometraje: {vehiculo.kilometraje} km")
        print("Estado de las ruedas:")
        for i in range(len(vehiculo.ruedas)):
            print(vehiculo.ruedas[i].estado)


def main():
    vehiculos = []

    # Parte 3: Completar código principal
    # Completar
    # Aquí debes instanciar los dos objetos pedidos
    # y agregarlos a la lista de vehículos
    mazda = Automovil(110, 2018)
    Yamaha=Moto(88,2022,  2)
    vehiculos.append(mazda)
    vehiculos.append(Yamaha)
    # NO MODIFICAR
    vehiculo = None

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))
            print()

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                if vehiculo is None and vehiculos:
                    vehiculo = vehiculos[0]
                if vehiculo is None:
                    print("Aún no hay vehículos...")
                else:
                    dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1

        print()


if __name__ == "__main__":
    main()
