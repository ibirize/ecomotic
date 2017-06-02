from pyowm import OWM, timeutils

class weather():
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")
    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()

    # Tiempo y temperatura actual en mondragon
    def recibirTemperatura(self):

        temperatura = self.w.get_temperature('celsius')
        tem = temperatura.get('temp')
        print(tem)

    def estaNublado(self):
        nublado = self.owm.daily_forecast("Mondragon, es")
        hayNubes = nublado.will_be_rainy_at(timeutils.next_hour())
        return  hayNubes

    def salidaSol(self):
        amanecer = self.w.get_sunrise_time('iso')
        horaAmanecer = int(amanecer[11:13]) + 2
        minutoAmanecer = int(amanecer[14:16])
        print('Hora amanecer =', horaAmanecer, ':', minutoAmanecer)


    def puestaSol(self):
        atardecer = self.w.get_sunset_time('iso')
        horaAtardecer = int(atardecer[11:13]) + 2
        minutoAtardecer = int(atardecer[14:16])
        print('Hora atardecer =', horaAtardecer, ':', minutoAtardecer)


    def rotacionPaneles(self):
        # inclinacion del panel solar latitud +18 grados en invierno y en verano la latitud -18 grados
        # Rotacion del panel

        minutosParaRotacion = ((self.horaAtardecer * 60) + 28) - ((self.horaAmanecer * 60) + 44)
        gradosPorMinuto = 180 / minutosParaRotacion
        print('Grados a rotar por minuto', gradosPorMinuto)








