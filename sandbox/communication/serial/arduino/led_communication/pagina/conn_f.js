var reader;
var readableStreamClosed;
var writer;
var writableStreamClosed;
data_ = "";
n_data = 0;
var command_id = -1;
var port;
readyScale = false;
resultAK_tare = String.fromCharCode(6);
ak_count = 0;

async function obtener_puerto(){
    try {
        // Prompt user to select any serial port.
        port = await navigator.serial.requestPort();
        //await port.open({ baudRate: 9600 });
        info = port.getInfo()
        console.log('Se obtuvo el puerto!! ' + info);
        console.log(info.usbVendorId);
        console.log(info.usbProdcutId);
    } catch {
        alert("Falla en la obtención del puerto de la báscula!!");
    }
}

function get_port(){
    console.log('get_port(): Se obtuvo el puerto!! ' + port.getInfo());
    return port;
}


async function conectarse_puerto(port_){
    try {
          // Prompt user to select any serial port.
          port = port_; //await navigator.serial.requestPort();
          await port.open({ baudRate: 9600 });
          listenToPort();

          textEncoder = new TextEncoderStream();
          writableStreamClosed = textEncoder.readable.pipeTo(port.writable);

          writer = textEncoder.writable.getWriter();
          console.log('Se conecto!!');
      } catch {
          alert("Serial Connection Failed");
      }
}


async function conectarse(){
    try {
          // Prompt user to select any serial port.
          port = await navigator.serial.requestPort();
          await port.open({ baudRate: 9600 });
          listenToPort();

          textEncoder = new TextEncoderStream();
          writableStreamClosed = textEncoder.readable.pipeTo(port.writable);

          writer = textEncoder.writable.getWriter();
          console.log('Se conecto!!');
      } catch {
          alert("Serial Connection Failed");
      }
}

async function desconectarse(){

    console.log('Esta bloqueado: ' + port.readable.locked);
    try {
          await reader.cancel();
          await readableStreamClosed.catch( () => {} );
          await writer.close();
          await writableStreamClosed.catch( () => {} );
          await port.close();
          console.log('Se desconecto!!');
      } catch(e) {
        console.log(e);
          alert("Serial Disconnection Failed");
      }
}

async function listenToPort() {
    const textDecoder = new TextDecoderStream();
    //const readableStreamClosed = port.readable.pipeTo(textDecoder.writable);
    readableStreamClosed = port.readable.pipeTo(textDecoder.writable);
    //const reader = textDecoder.readable.getReader();
    reader = textDecoder.readable.getReader();

    // Listen to data coming from the serial device.
    while (true) {
        const { value, done } = await reader.read();
        if (done) {
            // Allow the serial port to be closed later.
            //reader.releaseLock();
            break;
        }
        // value is a string.
        appendToData(value);
    }
}

async function appendToData(newStuff) {
    if(newStuff == '\n'){ // newStuff == '\r' || 
        console.log("FIN DE LINEA");
        check_data(data_);
        appendToTerminal(data_);
    }else{
        data_ = data_+newStuff;
    }
    
}

function check_data(data2check){
    ak = resultAK_tare + "\r\n";
    if(data2check == ak){
        console.log('Se recibio un AK!!! ');
        ak_count++;
        if(ak_count == 2){
            readyScale = true;
            ak_count = 0;
        }
    }
}

async function appendToTerminal() {
    console.log('Recibido [' + n_data +']: '+data_);
    n_data++;
    data_ = "";
}

async function sendSerialLine(dataToSend) {
    await writer.write(dataToSend+"\r");
    console.log("---- Datos enviados");
    //await writer.releaseLock();
}