import serial
import serial.tools.list_ports

class myXbee:
    RESOLUTION_2_mV = float(1200) / float(1024)

    puerto = serial.Serial()

    def __init__(self, baudrate):

        puertos = list(serial.tools.list_ports.comports())

        if (len(puertos) > 0):

            for i in range(0, len(puertos)):
                try:
                    self.puerto = serial.Serial(puertos[i].device, baudrate)
                    self.puerto.close()
                    self.puerto.open()
                    print 'Se ha encontrado un puerto serie disponible.'
                    return
                except serial.SerialException:
                    pass

            raise Exception('No se han encontrado puertos serie disponibles')
        else:
            raise Exception('No se han encontrado puertos serie!\n')

    def puertoSerieDisponible(self):
        puertos = list(serial.tools.list_ports.comports())

        if (len(puertos) > 0):
            availablePorts = False

            for i in range(0, len(puertos)):
                try:
                    ser = serial.Serial(puertos[i].device, 9600)
                                            #(port='/dev/ttyUSB0',
                                            #baudrate=9600,
                                            #parity=serial.PARITY_ODD,
                                            #stopbits=serial.STOPBITS_TWO,
                                            #bytesize=serial.SEVENBITS)
                    ser.close()
                    ser.open()
                    availablePorts = True
                    return puertos[i].device
                    break
                except serial.SerialException:
                    pass

            if not availablePorts:
                print 'No se han encontrado puertos serie disponibles'
        else:
            print 'No se han encontrado puertos serie!\n'


    def recibir(self):
        start_delimiter = bin(0)

        while start_delimiter != b'\x7E':
            start_delimiter = self.puerto.read()

        length = int(self.puerto.read(2).encode('hex'), 16)
        #length = int.from_bytes(self.puerto.read(2),byteorder='big')

        message = self.puerto.read(length)
        return message

    def frame2adcvalue(self, frame):

        frameEncode = frame.encode('hex')
        print 'frameEncode'
        print frameEncode
        voltage = int(frameEncode, 16) & 0x3FF
        #voltage = float(frame[-2:].encode('hex'), 16)
        print 'voltage'
        print voltage
        milivoltios = voltage*self.RESOLUTION_2_mV
        print 'milivoltios'
        print milivoltios
        return milivoltios

    def getFrameSource(self, frame):
        sourceAddress = frame[1:9]
        print int(sourceAddress.encode('hex'), 16)
        id_sensor = hex(int(sourceAddress.encode('hex'), 16))
        #return hex(int.from_bytes(sourceAddress,byteorder='big'))
        return id_sensor[:-1]


