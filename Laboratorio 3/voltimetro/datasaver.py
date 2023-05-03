#!/usr/bin/python3
import serial

ser = serial.Serial(
    port = '/tmp/ttyS1',\
    baudrate = 9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,
    timeout=0\
    )
#ser=serial.Serial('/tmp/ttyS1', 9600)
f = open('Tensiones.csv', 'w+')

print("connected to: "+ ser.portstr)

try:
    while True:
        for c in ser.read():
            c=chr(c)
            print(c, end= "")
            f.write(c)
except KeyboardInterrupt:
    print("\nInterrupción de Programa debido al usuario.")

finally:
    ser.close()
    f.close()


