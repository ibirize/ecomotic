from pyowm import OWM
import time
import os

class controlPaneles:
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")
    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()

    ABIERTO = False

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

        minutosParaRotacion = self.puestaSol(self)-self.salidaSol(self)
        gradosPorMinuto = 180 / minutosParaRotacion
        #print('Grados a rotar por minuto', gradosPorMinuto)
        hora =time.strftime("%H:%M") #Formato de 24 horas
        #print("Hora actual :", hora)
        #print("Hora actual :", hora[:2])
        #print("minuto actual :", hora[3:5])
        tiempoActual= (int(hora[:2])*60)+int(hora[3:5])
        grados = gradosPorMinuto * (tiempoActual-self.salidaSol(self))
        print("Grados: ",grados)
        gradosInt = int(grados)
        if(gradosInt<= 16):
            return "0x0000000%x" % gradosInt
        else:
            return "0x000000%x" % gradosInt



    def sacarPaneles(self):
        print('Se van a sacar los paneles a los grados', self.rotacionPaneles(self))
        posicionPaneles = self.rotacionPaneles(self)
       # os.system("devmem2 0xfffffff0 w "+posicionPaneles)
        self.ABIERTO==True



    def cerrarPaneles(self):
        print('Se van a guardar los paneles')
        posicionPaneles = 0x00000000
        # os.system("devmem2 0xfffffff0 w "+posicionPaneles)
        self.ABIERTO==False