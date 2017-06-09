from weather import weather
from controlPaneles import controlPaneles
from controlSensores import controlSensores
import threading


mes = b'0x74'

#try:

#xbee = myXbee(9600)

#message = xbee.recibir()

#print(message)

#print(xbee.frame2adcvalue(message))

#print(xbee.getFrameSource(message))


#except Exception as excepcion:
#    print(excepcion.args)


def main():
    recogerTiempo = True
    controlS = controlSensores()
    tiempo = weather()
    threading.Thread(target=controlS.control, name='Control de sensores').start()

    while(True):
        print("dentro while")
        if(recogerTiempo):#una vez al dia
            tiempo.recibirTemperatura()
            tiemp = tiempo.queTiempoHace()
            if tiemp==0:
                # haySol
                print("esta soleado")
                # sacarPaneles
                controlPaneles.sacarPaneles(controlPaneles)
            if tiemp==1:
                #estaNublado
                print("esta nublado")
            if tiemp == 2:
                #estaLloviendo
                print("esta lloviendo")
            if tiemp == 3:
                #estaNevando
                print("esta nevando")
            if tiemp == 4:
                #hayNiebla
                print("hay niebla")
            if tiemp == 5:
                #hayTormenta
                print("hay tormenta")
            if tiemp ==-1:
                print("Valor por defecto")
                #cerrarPaneles
            recogerTiempo = False

    #controlSensores.temperatura(controlSensores.valorTemperatura)
    #controlSensores.anemometro(controlSensores.viento)
    #controlSensores.luxometro(controlSensores.valorLuxes)



main()
