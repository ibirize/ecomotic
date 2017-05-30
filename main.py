from pyowm import OWM, timeutils
import serial
from myXbee import myXbee

owm = OWM('044c76bb9e1ffb5b8f4f4b250502566f')

obs = owm.weather_at_place('Mondragon,es')

w = obs.get_weather()
a= w.get_wind()
b=w.get_temperature('celsius')

print( 'ibai naiz',a,b)

mes = b'0x74'

ser = serial.Serial('COM3',9600)
ser.close()
ser.open()
while mes != b'\x7E':
    mes = ser.read()
ser.close()

xbee = myXbee('COM3',9600)

message = xbee.recibir()

print(message)

print(xbee.frame2adcvalue(message))

print(xbee.getFrameSource(message))
