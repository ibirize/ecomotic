from pyowm import OWM, timeutils

class weather():
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")
    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()
    tiempo = owm.daily_forecast("Mondragon, es")
    # Tiempo y temperatura actual en mondragon
    def recibirTemperatura(self):

        temperatura = self.w.get_temperature('celsius')
        tem = temperatura.get('temp')
        print(tem)

    def estaNublado(self):
        nublado = self.tiempo.will_be_cloudy_at(timeutils.next_hour())
        return  nublado

    def haceSol(self):
        soleado = self.tiempo.will_be_sunny_at(timeutils.next_hour())
        return soleado

    def hayTormenta(self):
        tormenta = self.tiempo.will_be_stormy_at(timeutils.next_hour())
        return tormenta

    def hayNiebla(self):
        niebla = self.tiempo.will_be_foggy_at(timeutils.next_hour())
        return  niebla

    def estaLloviendo(self):
        lluvia = self.tiempo.will_be_rainy_at(timeutils.next_hour())
        return lluvia

    def estaNevando(self):
        nieve = self.tiempo.will_be_snowy_at(timeutils.next_hour())
        return nieve



    def queTiempoHace(self):
        if(self.estaNublado(self)):
            return 0
        if(self.haceSol(self)):
            return 1
        if(self.estaLloviendo(self)):
            return 2
        if(self.estaNevando(self)):
            return 3
        if(self.hayNiebla(self)):
            return 4
        if(self.hayTormenta(self)):
            return 5


