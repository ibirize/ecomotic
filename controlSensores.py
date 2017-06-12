from  myXbee import *
from controlPaneles import controlPaneles

class controlSensores:

    ID_LM35="0x13a200400a42f6"
    ID_LUXOMETRO="0x13a200406a8ace"
    ID_ANEMOMETRO="0x13a200406a8aa3"
    TEMPERATURA_MINIMA=18
    TEMPERATURA_MAXIMA=23
    mV_A_Grados = 10
    VELOCIDAD_VIENTO_MAXIMA = 60
    valorLuxes = 0
    valorTemperatura = 0
    viento=0
    TEMPERATURA_ADECUADA=False
    SUFICIENTE_LUZ=False
    DEMASIADO_VIENTO=False

    paneles = controlPaneles()


    def __init__(self):
        pass

    def control(self):

        serial = False
        while (serial != True):

            try:

                xbee = myXbee(9600)
                message = xbee.recibir()
                serial = True


            except Exception as excepcion:
                    print(excepcion.args)

        while(True):
            mensajeRecibido = xbee.recibir()

            origenMensaje = xbee.getFrameSource(mensajeRecibido)

            if(origenMensaje==self.ID_LM35):
                print("LM35")
                valorTemperatura = xbee.frame2adcvalue(mensajeRecibido) / self.mV_A_Grados
                self.temperatura(valorTemperatura)

            if(origenMensaje==self.ID_LUXOMETRO):
                print("LUXOMETRO")
                valorLuxes = xbee.frame2adcvalue(mensajeRecibido)
                self.luxometro(valorLuxes)

            if(origenMensaje==self.ID_ANEMOMETRO):
                print("ANEMOMETRO")
                finDatos = mensajeRecibido.find(b'\x0D', 0, len(mensajeRecibido))
                datosAnemometro = mensajeRecibido[12:finDatos]
                viento = float(datosAnemometro)
                self.anemometro(viento)

    def luxometro(self, valorLuxes):

        luxes = (pow(10,(valorLuxes - 284.62) / 69.22)) / 0.092903
        if (luxes < 50 and  self.paneles.ABIERTO == True):
            self.paneles.cerrarPaneles()

        if (luxes > 50 and  self.paneles.ABIERTO == False):
            self.paneles.sacarPaneles()

    def anemometro(self, viento):



        if (viento < self.VELOCIDAD_VIENTO_MAXIMA and  self.paneles.ABIERTO == False):
            self.paneles.sacarPaneles()
            self.VALOR_ANEMOMETRO=1

        if (viento > self.VELOCIDAD_VIENTO_MAXIMA and  self.paneles.ABIERTO == True):
            self.paneles.cerrarPaneles()

    def temperatura(self, valorTemperatura):

        if (valorTemperatura < self.TEMPERATURA_MINIMA):
            self.paneles.subirPersiana()

        if (valorTemperatura > self.TEMPERATURA_MAXIMA):
            self.paneles.bajarPersiana()
        else:
            print("La temperatura es adecuada,", valorTemperatura)
