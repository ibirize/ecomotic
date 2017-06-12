from weather import weather
from controlPaneles import controlPaneles
from controlSensores import controlSensores
import threading
import time

mes = b'0x74'


def main():
    recogerTiempo = True
    proximaLecturaSegundos = 60
    controlS = controlSensores()
    paneles = controlPaneles()
    tiempo = weather()
    threading.Thread(target=controlS.control, name='Control de sensores').start()

    while(True):
        if(recogerTiempo==False):

            time.sleep(proximaLecturaSegundos)   #define el tiempo que tiene que esperar hasta
                            # realizar la proxima lectura del tiempo de la pagina web
            recogerTiempo=True

        if(recogerTiempo):#una vez al dia
            tiempo.recibirTemperatura()
            tiemp = tiempo.queTiempoHace()
            if tiemp==0:
                # haySol
                print("esta soleado")
                # sacarPaneles
                paneles.sacarPaneles()
            """ if tiemp==1:
                #estaNublado
                print("esta nublado")
                
            if tiemp == 2:
                #estaLloviendo
                print("esta lloviendo")
            if tiemp == 3:
                #estaNevando
                print("esta nevando")
            if tiemp == 4:
                #hayNiebla
                print("hay niebla")
            if tiemp == 5:
                #hayTormenta
                print("hay tormenta")
            #if tiemp ==-1:
             #   print("Valor por defecto")
                #cerrarPaneles
                """
            if tiemp!=0:
                print("Meteorologia desfavorable se guardarán los paneles")
                paneles.cerrarPaneles()
            recogerTiempo = False





main()
