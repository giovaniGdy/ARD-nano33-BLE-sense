import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())

def read_ports():
    conn_port = []

    for p in ports:
        conn_port.append(p)

    return conn_port
