import serial
import time
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

exit()
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
print(ser)

ser.open()

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
                data["peso"] = line[2:-2]
            else:
                data[counter] = line
            #print("Mensaje recibido {}: {}".format(counter, line))
            if(counter == counter_end):
                break
    return data

if ser.is_open:
    print("Se abrío!!!")

    ## comando .. Tara
    cmd="T\r"
    print("comando: {}".format(cmd))
    ser.write(cmd.encode())
    read_lines(ser, 0, 2)
    ## comando ...
    cmd="Q\r"
    print("comando: {}".format(cmd))
    ser.write(cmd.encode())
    data = read_lines(ser, 0, 4)
    print(data)
    #msg=ser.readline()
    #print("Mensaje recibido: {}".format(msg))
    cmd="Q\r"
    for i in range(100):
        time.sleep(0.25)
        ser.write(cmd.encode())
        data = read_lines(ser, 0, 4)
        if "peso" in data:
            print(data["peso"])
        else:
            print(data)

ser.close()