import serial
import time
import serial.tools.list_ports

ser = serial.Serial()

ack_ = b"\x06\r\n"

def list_ports_():
    data_ports = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        data_ports.append( {"port": port, "desc": desc} )
    return data_ports

def connect_port(port, baudrate):
    ser.baudrate = baudrate
    ser.port = port
    #ser.timeout = None
    try:
        ser.open()
        print("Abrio comunicación serial!!")
    except Exception as e:
        print("Error al abrir el puerto {}".format(port))

def disconnect_port():
    try:
       ser.close() 
       print("Desconexión exitosa!")
    except Exception as e:
        print("Error al desconectarse!!")

def tare_init():
    cmd = "T\r"
    ser.write(cmd.encode())
    data = read_lines(ser, 0, 2)
    for e in data:
        if data[e] == ack_:
            print("Tara inicializada ok!")
            return True
    print("Fallo al inicializar la tara")
    return False 

def ask_weight():
    cmd="Q\r"
    ser.write(cmd.encode())
    data = read_lines(ser, 0, 4)
    weight = {"weight": -1, "type": "--"}
    if "peso" in data:
        weight["weight"] = float(data["peso"][:-3])
        weight["type"] = str(data["peso"][-2:], 'utf-8')
    return weight

def read_lines(ser, counter_init, counter_end):
    counter = counter_init
    data = {}
    while True:
        line = ser.readline() # hasta que no recibe datos dejara de ejecutarse ... 
        if not line.strip():  # evaluates to true when an "empty" line is received
            print("Empty line!! --- salir")
            break
        else:
            counter+=1
            if(line[0:2] == b"ST" or line[0:2] == b"US"):
                data["peso"] = line[3:-2]
            else:
                data[counter] = line
            #print("Mensaje recibido {}: {}".format(counter, line))
            if(counter == counter_end):
                break
    return data