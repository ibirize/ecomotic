from pyowm import OWM, timeutils

def weather():
    owm = OWM("044c76bb9e1ffb5b8f4f4b250502566f")

    # Tiempo y temperatura actual en mondragon

    obs = owm.weather_at_place('Mondragon, es')
    w = obs.get_weather()
    print(w.get_temperature())

    f = owm.daily_forecast("Mondragon, es")
    print(f.will_be_sunny_at(timeutils.next_hour()))

    amanecer = w.get_sunrise_time('iso')
    atardecer = w.get_sunset_time('iso')

    print(w.get_sunrise_time('iso'))
    print(w.get_sunset_time('iso'))

    horaAmanecer = int(amanecer[11:13]) + 2
    minutoAmanecer = int(amanecer[14:16])
    print('Hora amanecer =', horaAmanecer, ':', minutoAmanecer)

    horaAtardecer = int(atardecer[11:13]) + 2
    minutoAtardecer = int(atardecer[14:16])
    print('Hora atardecer =', horaAtardecer, ':', minutoAtardecer)

    if f.will_be_sunny_at(timeutils.next_hour()) == True:
        # codigo para sacar paneles
        print('Se van a sacar los paneles')


    if f.will_be_sunny_at(timeutils.next_hour()) == False:
        # codigo para guardar los paneles
        print('Se van a guardar los paneles')

    # os.system("devmem2 0xfffffff0 w 0x1ff00210")

    # os.system("devmem2 0x1ff90000 w 0x00000001")


    # inclinacion del panel solar latitud +18 grados en invierno y en verano la latitud -18 grados
    # Rotacion del panel

    minutosParaRotacion = ((horaAtardecer * 60) + 28) - ((horaAmanecer * 60) + 44)
    gradosPorMinuto = 180 / minutosParaRotacion
    print('Grados a rotar por minuto', gradosPorMinuto)
    pass

weather()