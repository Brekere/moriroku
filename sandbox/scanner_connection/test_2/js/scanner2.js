var BarcodesScanner = {
    barcodeData: '',
    deviceId: '',
    symbology: '',
    timestamp: 0,
    dataLength: 0
};
data_ = '';
n_data = 0;
use_scanner = true;
function onScannerNavigate(barcodeData, deviceId, symbology, timestamp, dataLength){
    BarcodesScanner.barcodeData = barcodeData;
    BarcodesScanner.deviceId = deviceId;
    BarcodesScanner.symbology = symbology;
    BarcodesScanner.timestamp = timestamp;
    BarcodesScanner.dataLength = dataLength;
    $(BarcodesScanner).trigger('scan');
}

BarcodesScanner.tmpTimestamp = 0;
BarcodesScanner.tmpData = '';
$(document).on('keypress', function(e){
    e.stopPropagation();
    if(use_scanner){
        console.log('e.keyCode:' + e.keyCode + '   which:' + e.which + '    charCode:' + e.charCode + '   =>  char: ' +String.fromCharCode(e.charCode))
        var keycode = (e.keyCode ? e.keyCode : e.which);
        console.log('keycode: ' + keycode)
        if (BarcodesScanner.tmpTimestamp < Date.now() - 500){
            BarcodesScanner.tmpData = '';
            BarcodesScanner.tmpTimestamp = Date.now();
        }
        if (keycode == 13 && BarcodesScanner.tmpData.length > 0){
            onScannerNavigate(BarcodesScanner.tmpData, 'FAKE_SCANNER', 'WEDGE', BarcodesScanner.tmpTimestamp, BarcodesScanner.tmpData.length);
            BarcodesScanner.tmpTimestamp = 0;
            BarcodesScanner.tmpData = '';
            console.log('data_: ' + data_);
        } else if (e.charCode && e.charCode > 0) {
            BarcodesScanner.tmpData += String.fromCharCode(e.charCode);
            data_ += String.fromCharCode(e.charCode);
        }
    }
});

window.addEventListener("keydown", function(e) {
    //tested in IE/Chrome/Firefox
    //console.log('Key Down: e.key ' + e.key + '   ---   ' + e.Code)
    //document.getElementById("key").innerHTML = e.key;
    //document.getElementById("keyCode").innerHTML = e.keyCode;
    //document.getElementById("eventCode").innerHTML = e.code;
  })

var foo = function(){
    alert("hello from foo");
}


//var foo = 'bar';
var cleanup = function () {
    delete window.foo;
    delete window.cleanup;
};

// unload all resources
cleanup();


/*
GlobalModuleHandlerThingy.addModule('my_module', {
    create: function () {
        this.foo = 'bar';
        return this;
    },
    foo: null,
    destroy: function () {
        // unload events, etc.
    }
});

*/