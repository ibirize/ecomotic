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
    threading.Thread(target=controlSensores.control(controlSensores), name='Control de sensores')

    while(True):
        if(recogerTiempo):#una vez al dia
            weather.recibirTemperatura(weather)
            tiempo = weather.queTiempoHace(weather)
            if tiempo==0:
                # haySol
                print("esta soleado")
                # sacarPaneles
                controlPaneles.sacarPaneles(controlPaneles)
            if tiempo==1:
                #estaNublado
                print("esta nublado")
            if tiempo == 2:
                #estaLloviendo
                print("esta lloviendo")
            if tiempo == 3:
                #estaNevando
                print("esta nevando")
            if tiempo == 4:
                #hayNiebla
                print("hay niebla")
            if tiempo == 5:
                #hayTormenta
                print("hay tormenta")
            if tiempo ==-1:
                print("Valor por defecto")
                #cerrarPaneles
            recogerTiempo = False





main()
