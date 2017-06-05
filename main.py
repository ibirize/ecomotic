from weather import weather
from myXbee import myXbee




mes = b'0x74'

#try:

#xbee = myXbee(9600)

#message = xbee.recibir()

#print(message)

#print(xbee.frame2adcvalue(message))

#print(xbee.getFrameSource(message))


#except Exception as excepcion:
#    print(excepcion.args)



def main():
    serial = False
    recogerTiempo = True
   # while (serial != True):
    try:

            xbee = myXbee(9600)

            #message = xbee.recibir()
            #print(message)
            print(xbee)
            serial = True


            #print(xbee.frame2adcvalue(message))

            #print(xbee.getFrameSource(message))


    except Exception as excepcion:
            print(excepcion.args)

    while(1):
        if(recogerTiempo):
            weather.recibirTemperatura(weather)
            tiempo = weather.queTiempoHace(weather)
            if tiempo==0:
                #estaNublado
                print("esta nublado")
            if tiempo==1:
                #haySol
                print("esta soleado")
            if tiempo == 2:
                #estaLloviendo
                print("esta lloviendo")
            if tiempo == 3:
                #estaNevando
                print("esta nevando")
            if tiempo == 4:
                #hayNiebla
                print("hay niebla")
            if tiempo == 5:
                #hayTormenta
                print("hay tormenta")
            recogerTiempo = False


main()
nubes = weather.estaNublado(weather)
print(nubes)

#if nubes.will_be_sunny_at(timeutils.next_hour()) == True:
    # codigo para sacar paneles
  #  print('Se van a sacar los paneles')

#if nubes.will_be_sunny_at(timeutils.next_hour()) == False:
    # codigo para guardar los paneles
 #   print('Se van a guardar los paneles')

    # os.system("devmem2 0xfffffff0 w 0x1ff00210")

    # os.system("devmem2 0x1ff90000 w 0x00000001")
#