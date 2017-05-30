import serial

class myXbee:
    RESOLUTION_2_TEMPERATURE = 330/1024

    puerto = serial.Serial()

    def __init__(self, puertoSerie, baudrate):
        self.puerto = serial.Serial(puertoSerie,baudrate)
        self.puerto.close()
        self.puerto.open()


    def recibir(self):
        start_delimiter = bin(0)

        while start_delimiter != b'\x7E':
            start_delimiter = self.puerto.read()

        length = int.from_bytes(self.puerto.read(2),byteorder='big')

        message = self.puerto.read(length)

        return message

    def frame2adcvalue(self,frame):
        voltage = int.from_bytes(frame,byteorder='big') & 0x3FF
        temperature = voltage*self.RESOLUTION_2_TEMPERATURE
        return temperature

    def getFrameSource(self,frame):
        sourceAddress = frame[1:9]
        return hex(int.from_bytes(sourceAddress,byteorder='big'))

