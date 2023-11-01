import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def takePicture():
    arduino.write(bytes('c', 'utf-8'))
    time.sleep(5)
    data = arduino.readline()
    
    with open('data.txt', 'wb') as data_file:
        data_file.write(data)
    
    return data