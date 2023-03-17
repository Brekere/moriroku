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
info_comp = {};
list_info_comp = [];
n_elem_info_comp = 0;
init_comp = false;

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
