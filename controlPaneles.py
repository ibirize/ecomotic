from pyowm import OWM
import time
import os

class controlPaneles:
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")
    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()

    PANELES_FUERA = False
    PERSIANA_SUBIDA = False
    GRADOS_A_ROTAR = 180

    def salidaSol(self):
        amanecer = self.w.get_sunrise_time('iso')
        horaAmanecer = int(amanecer[11:13]) + 2
        minutoAmanecer = int(amanecer[14:16])
        #print('Hora amanecer =', horaAmanecer, ':', minutoAmanecer)
        minutosSalida = horaAmanecer*60 + minutoAmanecer
        return  minutosSalida


    def puestaSol(self):
        atardecer = self.w.get_sunset_time('iso')
        horaAtardecer = int(atardecer[11:13]) + 2
        minutoAtardecer = int(atardecer[14:16])
        #print('Hora atardecer =', horaAtardecer, ':', minutoAtardecer)
        minutos = horaAtardecer*60+minutoAtardecer
        return minutos


    def rotacionPaneles(self):
        # inclinacion del panel solar latitud +18 grados en invierno y en verano la latitud -18 grados
        # Rotacion del panel

        minutosParaRotacion = self.puestaSol()-self.salidaSol()
        gradosPorMinuto = float(self.GRADOS_A_ROTAR) / float(minutosParaRotacion)
        hora =time.strftime("%H:%M") #Formato de 24 horas
        tiempoActual= (int(hora[:2])*60)+int(hora[3:5])
        grados = gradosPorMinuto * (tiempoActual-self.salidaSol())
        gradosInt = int(grados)
        if(gradosInt<= 16):
            print 'Grados:', gradosInt
            return "0x0000000%x" % gradosInt
        else:
            print 'Grados:', gradosInt
            return "0x000000%x" % gradosInt



    def sacarPaneles(self):
        self.PANELES_FUERA=True
        posicionPaneles = self.rotacionPaneles()
        print 'Sacando paneles a los grados', posicionPaneles
        os.system("echo devmem2 0x41210000 w " + posicionPaneles)
        self.PANELES_FUERA = True

    def cerrarPaneles(self):
        print 'Guardando los paneles'
        self.PANELES_FUERA=False
        posicionPaneles = '0x00000000'
        os.system("echo devmem2 0x41210000 w " + posicionPaneles)
        self.PANELES_FUERA = False

    def bajarPersiana(self):
        if(self.PERSIANA_SUBIDA==True):
            print 'Se va a bajar la persiana'
            posicionPersiana = '0x00000000'
            os.system("echo devmem2 0x41210004 w " + posicionPersiana)
        self.PERSIANA_SUBIDA = False

    def subirPersiana(self):
        print 'Se va a subir la persiana'
        gradosInt = 180
        posicionPersiana = "0x000000%x" % gradosInt
        os.system("echo devmem2 0x41210004 w " + posicionPersiana)
        self.PERSIANA_SUBIDA = True




