import serial
import time
from tkinter import *

def takePicture(selected_port):
    if (selected_port == "Select Arduino COM"):
        data = "Error 0: No arduino selected"
    else:
        port_select = selected_port.split()[0]

        arduino = serial.Serial(port=port_select, baudrate=9600, timeout=.1)

        arduino.write(bytes('c', 'utf-8'))
        time.sleep(5)
        data = arduino.readline()
        try:
            int(data, 16)
        except:
            data = "Error 2: No arduino response."
            
        else:
            with open('temp/data.txt', 'wb') as data_file:
                data_file.write(data)
            data = "Ok"

    return data
