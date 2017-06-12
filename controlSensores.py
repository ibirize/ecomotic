from  myXbee import *
from controlPaneles import controlPaneles

class controlSensores:

    LM35="0x13a200400a42f6"
    LUXOMETRO="0x13a200406a8ace"
    ANEMOMETRO="0x13a200406a8aa3"
    TEMPERATURA_MINIMA=18
    TEMPERATURA_MAXIMA=23
    mV_A_Grados = 10
    VELOCIDAD_VIENTO_MAXIMA = 30
    valorLuxes = 0
    valorTemperatura = 0
    viento=0

    def __init__(self):
        pass

    def control(self):

        serial = False
        while (serial != True):

            try:

                xbee = myXbee(9600)

                message = xbee.recibir()
                print(message)
                print(xbee)
                serial = True

                print(xbee.frame2adcvalue(message))

                print(xbee.getFrameSource(message))


            except Exception as excepcion:
                    print(excepcion.args)

        while(True):
            mensajeRecibido = xbee.recibir()

            origenMensaje = xbee.getFrameSource(mensajeRecibido)

            if(origenMensaje==self.LM35):
                valorTemperatura = xbee.frame2adcvalue(mensajeRecibido) / self.mV_A_Grados

                self.temperatura(valorTemperatura)

            if(origenMensaje==self.LUXOMETRO):
                valorLuxes = xbee.frame2adcvalue(mensajeRecibido)
                self.luxometro(valorLuxes)

            if(origenMensaje==self.ANEMOMETRO):
                viento = xbee.frame2adcvalue(mensajeRecibido)
                self.anemometro(viento)

    def luxometro(self, valorLuxes):


        luxes = (pow(10,(valorLuxes - 284.62) / 69.22)) / 0.092903
        if (luxes < 50 and controlPaneles.ABIERTO == True):
            controlPaneles.cerrarPaneles(controlPaneles)

        if (luxes > 50 and controlPaneles.ABIERTO == False):
            controlPaneles.sacarPaneles(controlPaneles)

    def anemometro(self, viento):



        if (viento < self.VELOCIDAD_VIENTO_MAXIMA and controlPaneles.ABIERTO == False):
            controlPaneles.sacarPaneles(controlPaneles)
        if (viento > self.VELOCIDAD_VIENTO_MAXIMA and controlPaneles.ABIERTO == True):
            controlPaneles.sacarPaneles(controlPaneles)

    def temperatura(self, valorTemperatura):

        if (valorTemperatura < self.TEMPERATURA_MINIMA):
            print("Subir persianas", valorTemperatura)
            controlPaneles.subirPersiana(controlPaneles)
        if (valorTemperatura > self.TEMPERATURA_MAXIMA):
            print("Bajar persianas", valorTemperatura)
            controlPaneles.bajarPersiana(controlPaneles)
        else:
            print("La temperatura es adecuada,", valorTemperatura)
