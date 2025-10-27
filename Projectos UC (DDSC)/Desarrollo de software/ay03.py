import random
import ampolleta_nueva as am
    

class Ampolleta:
    def __init__(self):
        self.encendida = False
        self.quemada = False
        self.probabilidad_quemarse = random.randint(*am.p_falla_de_fabrica)/100

    def encender(self):
        if not self.quemada:
            if not self.encendida:
                self.encendida = True
                print("La ampolleta se ha encendido.")
            else:
                print("La ampolleta ya está encendida.")
            self.actualizar_probabilidad_quemarse()
        else:
            print("La ampolleta está quemada y no se puede encender.")

    def apagar(self):
        if not self.quemada:
            if self.encendida:
                self.encendida = False
                print("La ampolleta se ha apagado.")
            else:
                print("La ampolleta ya está apagada.")
            self.actualizar_probabilidad_quemarse()
        else:
            print("La ampolleta está quemada y no se puede apagar.")

    def actualizar_probabilidad_quemarse(self):
        # Aumentar la probabilidad de quemarse con cada encendido y apagado
        if not self.encendida:
            self.probabilidad_quemarse += 0.05
        if self.probabilidad_quemarse > 1:
            self.quemar()

    def quemar(self):
        self.quemada = True
        print("La ampolleta se ha quemado y necesita ser reemplazada.")

    def __str__(self):
        estado = "encendida" if self.encendida else "apagada"
        if self.quemada:
            return "Ampolleta (quemada)"
        return f"Ampolleta ({estado})"
    
    def __repr__(self):
        return str(self.encendida)


class Lampara:
    # Necesito que inicie con una ampolleta, reciba una marca como parametro 
    # y una caja de ampolletas de reemplazo (3)
    def __init__(self, marca):
        self.marca = marca #string
        self.ampolleta = Ampolleta() #objeto de clase Ampolleta
        self.ampolletas_de_reemplazo = [Ampolleta() for _ in range(3)]

    # Solo voy a cambiar la ampolleta si esta esta quemada
    def cambiar_ampolleta(self, ampolleta_nueva):
        if self.ampolleta.quemada:
            self.ampolleta = ampolleta_nueva
        else:
            print("No necesito reemplazarla, no esta quemada")

    # Necisto saber si la ampolleta esta quemada o no. Si no, la enciendo
    # Si esta quemada, la reemplazo por una que este en las ampolletas de reemplazo
    # Si no me quedan, imprimo
    def encender_lampara(self):
        if not self.ampolleta.quemada:
            self.ampolleta.encender()
        else:
            if len(self.ampolletas_de_reemplazo) > 0:
                ampolleta_nueva = self.ampolletas_de_reemplazo.pop()
                self.cambiar_ampolleta(ampolleta_nueva)
            else:
                print("No me quedan ampolletas de reemplazo")

    def apagar_lampara(self):
        self.ampolleta.apagar()

   
    # Revisar si alguna ampolleta de reemplazo esta quemada
    def checkear_ampolletas_reemplaso(self):
        for ampolleta in self.ampolletas_de_reemplazo:
            if ampolleta.quemada:
                print("Tengo una ampolleta quemada en mi caja de reemplazos")
                return
        print("Todas mis ampolletas estan buenas")


    def __str__(self):
        return f"Lámpara con {self.ampolleta}"


# Ejemplo de uso
lampara_1 = Lampara("Lamparitas s.a.")

lampara_1.encender_lampara()
print(lampara_1)

ampolleta_1 = Ampolleta()
ampolleta_2 = Ampolleta()

ampolleta_2.quemada = True

var = str(ampolleta_1)
print(var) 
print(ampolleta_2.quemada) #True

# Caja de 3 ampolletas
caja_de_ampolletas = []

for _ in range(3):
    caja_de_ampolletas.append(Ampolleta())

caja_de_ampolletas = [Ampolleta(), Ampolleta(), Ampolleta()]

caja_de_ampolletas = [Ampolleta() for _ in range(3)]

for _ in range(10):
    lampara_1.encender_lampara()
    lampara_1.apagar_lampara()

for ampolleta in caja_de_ampolletas:
    ampolleta.encender()
    print(ampolleta.quemada)

lampara_1.encender_lampara()  # Intentar encender una lampara con la ampolleta quemada

ampolleta_nueva = caja_de_ampolletas.pop() #sacar el ultimo elemento de la lista
print(caja_de_ampolletas) #[Ampolleta()]