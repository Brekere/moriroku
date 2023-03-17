import serial
import time
import serial.tools.list_ports

MAX_WAITING_TIME = 0.5
ack_ = b"\x06\r\n"
BAUDRATE = 9600
port_descript_expected = "Prolific USB-to-Serial Comm Port"
ser = serial.Serial()

def list_ports_():
    data_ports = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        data_ports.append( {"port": port, "desc": desc} )
    return data_ports

def auto_connect():
    l_ports = list_ports_()
    print(l_ports)
    for port in l_ports:
        if "desc" in port:
            result = port["desc"].find(port_descript_expected)
            if result != -1:
                print("Encontro Puerto esperado: {},  desc: {}".format(port["port"], port["desc"]))
                return connect_port(port["port"], BAUDRATE)
    print("No encontro el puerto!!!")
    return False

def connect_port(port, baudrate):
    #ser.timeout = None
    connected = True
    try:
        ser.baudrate = baudrate
        ser.port = port
        ser.open()
        print("Abrio comunicación serial!!")
    except Exception as e:
        print("Error al abrir el puerto {}".format(port))
        disconnect_port()
        connected = False 
    return connected

def disconnect_port():
    try:
       ser.close() 
       print("Desconexión exitosa!")
    except Exception as e:
        print("Error al desconectarse!!")

def tare_init():
    cmd = "T\r"
    try:
        ser.write(cmd.encode())
        data = read_lines(ser, 0, 2)
    except Exception as e:
        print("Fallo de escritura en puertos")
        return False 
    for e in data:
        if data[e] == ack_:
            print("Tara inicializada ok!")
            return True
    print("Fallo al inicializar la tara")
    return False 

def ask_weight():
    cmd="Q\r"
    weight = {}
    try:
        ser.write(cmd.encode())
        data = read_lines(ser, 0, 4)
    except Exception as e:
        return {"weight": -1, "type": "--", "error": True, "error_info": "Error en escritura del bufer serial"} 
    if "peso" in data:
        try:
            weight["weight"] = float(data["peso"][:-3])
            weight["type"] = str(data["peso"][-2:], 'utf-8')
            weight["error"] = data["error"]
        except Exception as e:
            weight["weight"] = -1
            weight["type"] = "--"
            weight["error"] = True
            weight["info_error"] = "erorr de conversión de información de la báscula: " + str(e)
            return weight
        if data["error"]:
            weight["info_error"] = data["info_error"]
    return weight

def read_lines(ser, counter_init, counter_end):
    counter = counter_init
    data = {"error": False}
    start_time = time.time()
    while True:
        line = ser.readline() # hasta que no recibe datos dejara de ejecutarse ... 
        if not line.strip():  # evaluates to true when an "empty" line is received
            print("Empty line!! --- salir")
            break
        else:
            if time.time() - start_time > MAX_WAITING_TIME: # esperar a lo más medio segundo
                print("Se alcanzo el tiempo máximo de espera de recolección de datos predefinido")
                break
            counter+=1
            if(line[0:2] == b"ST" or line[0:2] == b"US"):
                data["peso"] = line[3:-2]
            else:
                data[counter] = line
            if(counter == counter_end):
                break
    if "peso" not in data:
        data["peso"] = "-1.0kg"
        data["error"] = True
        data["info_error"] = "Internal error en lectura del bufer del puerto"
    return data