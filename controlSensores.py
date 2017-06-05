from  myXbee import *
from controlPaneles import controlPaneles

class controlSensores:

    LM35=15
    LUXOMETRO=25
    ANEMOMETRO=35
    TEMPERATURA_MINIMA=18
    TEMPERATURA_MAXIMA=23
    mV_A_Grados = 10
    VELOCIDAD_VIENTO_MAXIMA = 30


    def control(self):

        serial = False
       # while (serial != True):

        try:

            xbee = myXbee(9600)

            #message = xbee.recibir()
            message=b'hola'
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
                self.temperatura(xbee, mensajeRecibido)

            if(origenMensaje==self.LUXOMETRO):
               self.luxometro(xbee, mensajeRecibido)

            if(origenMensaje==self.ANEMOMETRO):
                self.anemometro(xbee, mensajeRecibido)

    def luxometro(self, xbee, mensajeRecibido):

        valorLuxes = xbee.frame2adcvalue(mensajeRecibido)

        luxes = (10 * pow((valorLuxes - 284.62) / 69.22)) / 0.092903
        if (luxes < 50 and controlPaneles.ABIERTO == True):
            controlPaneles.cerrarPaneles(controlPaneles)

        if (luxes > 50 and controlPaneles.ABIERTO == False):
            controlPaneles.sacarPaneles(controlPaneles)

    def anemometro(self, xbee, mensajeRecibido):

        viento = xbee.frame2adcvalue(mensajeRecibido)

        if (viento < self.VELOCIDAD_VIENTO_MAXIMA and controlPaneles.ABIERTO == False):
            controlPaneles.sacarPaneles(controlPaneles)
        if (viento > self.VELOCIDAD_VIENTO_MAXIMA and controlPaneles.ABIERTO == True):
            controlPaneles.sacarPaneles(controlPaneles)

    def temperatura(self, xbee, mensajeRecibido):

        valorTemperatura = xbee.frame2adcvalue(mensajeRecibido) / self.mV_A_Grados

        if (valorTemperatura < self.TEMPERATURA_MINIMA):
            print("Subir persianas", valorTemperatura)
        if (valorTemperatura > self.TEMPERATURA_MAXIMA):
            print("Bajar persianas", valorTemperatura)
