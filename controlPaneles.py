from pyowm import OWM


class controlPaneles:
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")
    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()
    def salidaSol(self):
        amanecer = self.w.get_sunrise_time('iso')
        horaAmanecer = int(amanecer[11:13]) + 2
        minutoAmanecer = int(amanecer[14:16])
        print('Hora amanecer =', horaAmanecer, ':', minutoAmanecer)
        minutosSalida = horaAmanecer*60 + minutoAmanecer
        return  minutosSalida


    def puestaSol(self):
        atardecer = self.w.get_sunset_time('iso')
        horaAtardecer = int(atardecer[11:13]) + 2
        minutoAtardecer = int(atardecer[14:16])
        print('Hora atardecer =', horaAtardecer, ':', minutoAtardecer)
        minutos = horaAtardecer*60+minutoAtardecer
        return minutos


    def rotacionPaneles(self):
        # inclinacion del panel solar latitud +18 grados en invierno y en verano la latitud -18 grados
        # Rotacion del panel

        minutosParaRotacion = self.puestaSol(self)-self.salidaSol(self)
        gradosPorMinuto = 180 / minutosParaRotacion
        print('Grados a rotar por minuto', gradosPorMinuto)


