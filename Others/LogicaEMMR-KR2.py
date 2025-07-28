#variables
from operator import truediv

from fontTools.misc.cython import returns
from sympy import false
from sympy.strategies.core import switch

Mill_type=1
_seqTask=1
#seq task
NTaskEndOK=900
NTaskEndNoOK=910
NTaskEndPaused=920
NTaskEndCancel=930
NTaskEndFault=940
_thereIsScan=False
ExistenPernos=False
I_needBolt=False
pernoIgualAlSolicitado=False

def rack():
    print("ejecutando funcion de rack")
    global _seqTask
    while (_seqTask < 1000):
        match _seqTask:
            case 60:
                print("comienza proce de escaner")
                _seqTask=61
            case 61:
                print("escaneado...")
                _thereIsScan = True
                _seqTask = 70
            case 70:
                _thereIsScan = True
                PernosOk=input("existen pernos? s/n\n")
                if PernosOk=="n":
                    print("NO existen pernos")
                    break
                else:
                    _seqTask=71
            case 71:
                consulta1=input("requiere pernos? s/n: \n")
                if consulta1=="s":
                    consulta2 = input("perno tomado igual al solicitado? s/n: \n")
                    if consulta1=="s":
                        print("perno correcto")
                        _seqTask=80
                    else:
                        print("perno distinto\n Regresando a HOME")
            case 80:
                decision=input("el elemento puede ser tomado?s/n\n")
                if decision:
                    _seqTask=90
                else:
                    print("vuelve al Home")
            case 90:
                print("nuevamente escanea para confirmar presencia")
                presencia=input("esta el perno realmente?\n")
                if presencia:
                    _seqTask=100
                else:
                    print("vuelve al Home")
            case 100:
                print("va a tomar el elemento, siguiente secuencia s/n?\n")
                _seqTask=110
            case 110:
                print("ok mañana sigo")


def bandeja():
    print("ejecutando secuencia de bandejas...")
    return _seqTask


while (_seqTask<1000):
    match _seqTask:
        case 1:
            print("case 1")
            var=input("set param en PLC\nsqte secuencia? s/n\n")
            var.rstrip().lower().lstrip()
            if var=="s":
                _seqTask=10
            else:
                _seqTask=NTaskEndFault
        case 10:
            print("case 10")
            var = input("REVISION SISTEMA NEUMATICO\nSys Neu OK?, s/n\n")
            var.rstrip().lower().lstrip()
            if var == "s":
                _seqTask = 20
            else:
                _seqTask = NTaskEndFault
        case 20:
            print("case 20")
            var = input("REVISION ESTADO DE LA GARRA Y POSICION ROBOT,\n?, se encuentran ok s/n\n")
            var.rstrip().lower().lstrip()
            if var == "s":
                _seqTask = 30
            else:
                _seqTask = NTaskEndFault
        case 30:
            print("case 30")
            var = input("recuperacion de posicion HOME\nPosicion OK?, s/n\n")
            var.rstrip().lower().lstrip()
            if var == "s":
                _seqTask = 40
            else:
                _seqTask = NTaskEndFault
        case 40:
            print("case 40")
            var = input("revision de sensor SCAN\nsensor ok?, s/n\n")
            var.rstrip().lower().lstrip()
            if var == "s":
                _seqTask = 50
            else:
                _seqTask = NTaskEndFault
        case 50:
            print("case 50")
            var = input("REVISION SI SE ESCANEARON LOS PERNOS EN RACK O BANDEJAS?\nsensados?, s/n\n")
            var.rstrip().lower().lstrip()
            if var == "s":
                if Mill_type==1 or Mill_type==2:
                    _seqTask = 70
                    envia=1
                    var=rack()
            else:
                print("no sensado, debe sensar, ir a sensar")
                _seqTask = 60
                rack()

        case 130:
            print("vuelve de ejecutar sub-funciones")
            _seqTask = 4









