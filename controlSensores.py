from  myXbee import *
from controlPaneles import controlPaneles

class controlSensores:

    ID_LM35="0x13a200400a42f6"
    ID_LUXOMETRO="0x13a200406a8ace"
    ID_ANEMOMETRO="0x13a200406a8aa3"
    TEMPERATURA_MINIMA=18
    TEMPERATURA_MAXIMA=23
    mV_A_Grados = 10
    VELOCIDAD_VIENTO_MAXIMA = 10
    valorLuxes = 0
    valorTemperatura = 0
    viento=0
    TEMPERATURA_ADECUADA=True
    SUFICIENTE_LUZ=True
    DEMASIADO_VIENTO=True

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

        luxes = (pow(10,((valorLuxes/2) - 284.62) / 69.22)) / 0.092903
        if (luxes < 50 and  self.paneles.PANELES_FUERA == True):
            print 'Se van a guardar los paneles, no hay suficiente luz ', luxes, 'luxes'
            self.paneles.cerrarPaneles()
            self.SUFICIENTE_LUZ = False

        elif (luxes > 50 and  self.paneles.PANELES_FUERA == False):
            if(self.DEMASIADO_VIENTO==False):
                print 'Se van a sacar los paneles, hay suficiente luz ', luxes, 'luxes'
                self.paneles.sacarPaneles()
            else:
                print 'No hay datos sobre el viento o aun no se han recibido, aun no se sacan los paneles'
            self.SUFICIENTE_LUZ = True
        else:
            if(self.paneles.PANELES_FUERA == True):
                print 'Los paneles seguiran fuera, suficiente luz'
            else:
                print 'Los paneles seguiran guardados, poca luz'



    def anemometro(self, viento):



        if (viento < self.VELOCIDAD_VIENTO_MAXIMA and  self.paneles.PANELES_FUERA == False):
            if(self.SUFICIENTE_LUZ==True):
                print 'Se van a sacar los paneles, el viento es', viento
                self.paneles.sacarPaneles()
            else:
                print 'Aun no hay datos del luxometro, se esperara para sacar los paneles'
            self.DEMASIADO_VIENTO = False

        elif (viento > self.VELOCIDAD_VIENTO_MAXIMA and  self.paneles.PANELES_FUERA == True):
            print 'Se van a guardar los paneles, el viento es ', viento
            self.paneles.cerrarPaneles()
            self.DEMASIADO_VIENTO = True

        else:
            if(self.paneles.PANELES_FUERA == True):
                print 'Los paneles seguiran fuera, poco viento'
            else:
                print 'Los paneles seguiran guardados, demasiado viento'

    def temperatura(self, valorTemperatura):

        if (valorTemperatura < self.TEMPERATURA_MINIMA and self.paneles.PERSIANA_SUBIDA == False):
            self.TEMPERATURA_ADECUADA=False
            if(self.TEMPERATURA_ADECUADA == False):
                self.paneles.subirPersiana()

        if (valorTemperatura > self.TEMPERATURA_MAXIMA and self.paneles.PERSIANA_SUBIDA == True):
            self.TEMPERATURA_ADECUADA = False
            if (self.TEMPERATURA_ADECUADA == False):
                self.paneles.bajarPersiana()
        else:
            self.TEMPERATURA_ADECUADA = True
            print 'La temperatura es adecuada', valorTemperatura
