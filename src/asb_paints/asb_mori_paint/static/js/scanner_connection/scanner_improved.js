let current_month_qr = undefined
let current_year_qr = undefined
let lote_component = undefined
let identifier = undefined
let contenedor = false
let component_supplier = undefined
let unit_of_measure_w = undefined
let special_case_ln245 = false 
let num_lines_special_case = 5 // cambiar de acuerdo a lo esperado ... (supeior para ver si ahí para o no )
let id_process_ = localStorage.getItem('id_process')
let expiration_date = undefined

struct_realese_process = {
    "id_process" : "",
    "id_worker" : "",
    "id_type_release" : "",
    "time_stamp" : "",
    "id_component_tare" : "",
    "id_container" : ""
}

var BarcodesScanner = {
    barcodeData: '',
    deviceId: '',
    symbology: '',
    timestamp: 0,
    dataLength: 0
};

line_counter_qr = 0
data_ = '';
n_data = 0;
use_scanner = true;
reading_qr = false;
relase_expires_restriction = false;
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

function init_setup_scanner(option){
    switch (option) {
        case 1:
            use_scanner = true //Opcionde lectura de codigo de barras de contenedor y validación del trabajador
            break;
        case 2:
            use_scanner = true
            reading_qr = true //delimitar el scaner para leer el qr de los componentes para verificar/validar caducidad
            line_counter_qr = 0
            break            
        case 3:
            use_scanner = true
            relase_expires_restriction = true 
            reading_qr = true
            break
        case 4:
            use_scanner = true
            reading_qr = true //delimitar el scaner para leer el qr de los componentes para verificar/validar caducidad
            line_counter_qr = 0
            special_case_ln245 = true
            break
        default:
            use_scanner = false
            relase_expires_restriction = false
            reading_qr = false
            break;
    }
}

function key_data_by_counter_line(){
    switch (line_counter_qr){
        case 0: // Proveedor
            component_supplier = data_
            break;
        case 1: // Identificador del componente
            identifier = data_
            break;
        case 2: // Numero de Lote
            batch_component_tare = data_
            break;
        case 3: // Peso del componente
            lote_component = parseInt(data_)
            break;
        case 4: // Unidad de medida
            unit_of_measure_w = data_
            break;
        case 5: // Fecha
            let array_data = data_.split('.')
            if(array_data.length == 2) {
                current_month_qr = parseInt(array_data[0])
                current_year_qr = parseInt(array_data[1])
            }
            break;
    }
}

function key_data_by_counter_line_2(){ // Caso del LN245
    console.log("line:", line_counter_qr, " data: ", data_)
    switch (line_counter_qr){
        case 0: // Proveedor
            component_supplier = data_
            break;
        case 1: // Identificador del componente
            identifier = data_
            break;
        case 2: // Numero de Lote
            batch_component_tare = data_
            break;
        case 3: // Valor 0
            lote_component = parseInt(data_)
            break;
        case 5: // espacio en blanco
            unit_of_measure_w = data_
            break;
        case 4:// Fecha
            let array_data = data_.split('.')
            if(array_data.length == 2) {
                current_month_qr = parseInt(array_data[0])
                current_year_qr = parseInt(array_data[1])
            }
            break;
        case 7: // Otra linea en blanco ... 
            break;
        case 8: // otra linea en blanco
            break;
    }
}

BarcodesScanner.tmpTimestamp = 0;
BarcodesScanner.tmpData = '';
$(document).on('keypress', function(e){
    e.stopPropagation();
    if(use_scanner){
        if(reading_qr){
            /* console.log('e.keyCode:' + e.keyCode + '   which:' + e.which + '    charCode:' + e.charCode + '   =>  char: ' +String.fromCharCode(e.charCode)) */
            var keycode = (e.keyCode ? e.keyCode : e.which);
            /* console.log('keycode: ' + keycode) */
            if (BarcodesScanner.tmpTimestamp < Date.now() - 500){
                BarcodesScanner.tmpData = '';
                BarcodesScanner.tmpTimestamp = Date.now();
            }
            if (keycode == 13 && BarcodesScanner.tmpData.length > 0){
                onScannerNavigate(BarcodesScanner.tmpData, 'FAKE_SCANNER', 'WEDGE', BarcodesScanner.tmpTimestamp, BarcodesScanner.tmpData.length);
                BarcodesScanner.tmpTimestamp = 0;
                BarcodesScanner.tmpData = '';
                console.log('data_: ' + data_);                
                if(special_case_ln245 == true){
                    key_data_by_counter_line_2();
                    data_ = ''
                    line_counter_qr += 1
                    if(line_counter_qr == num_lines_special_case){
                        if(contenedor == false){
                            validationQRComponentInformation()
                        } else {
                            validationQRPaitInformation()
                        }
                        line_counter_qr = -1
                        special_case_ln245 = false
                    }
                }else{
                    key_data_by_counter_line();
                    data_ = ''
                    line_counter_qr += 1 
                    if(line_counter_qr == 6){
                        if(contenedor == false){
                            validationQRComponentInformation()
                        } else {
                            validationQRPaitInformation()
                        }
                        line_counter_qr = -1
                    }
                }
            } else if (e.charCode && e.charCode > 0) {
                BarcodesScanner.tmpData += String.fromCharCode(e.charCode);
                data_ += String.fromCharCode(e.charCode);
                /* console.log(String.fromCharCode(e.charCode)) */
            }
        } else{            
            /* console.log('e.keyCode:' + e.keyCode + '   which:' + e.which + '    charCode:' + e.charCode + '   =>  char: ' +String.fromCharCode(e.charCode)) */
            var keycode = (e.keyCode ? e.keyCode : e.which);
            /* console.log('keycode: ' + keycode) */
            if (BarcodesScanner.tmpTimestamp < Date.now() - 500){
                BarcodesScanner.tmpData = '';
                BarcodesScanner.tmpTimestamp = Date.now();
            }
            if (keycode == 13 && BarcodesScanner.tmpData.length > 0){
                onScannerNavigate(BarcodesScanner.tmpData, 'FAKE_SCANNER', 'WEDGE', BarcodesScanner.tmpTimestamp, BarcodesScanner.tmpData.length);
                BarcodesScanner.tmpData = '';
                console.log('data_: ' + data_);
            } else if (e.charCode && e.charCode > 0) {
                BarcodesScanner.tmpData += String.fromCharCode(e.charCode);
                data_ += String.fromCharCode(e.charCode);
                /* console.log(String.fromCharCode(e.charCode)) */
            }
        }
    }
});

function validationQRComponentInformation(){
    console.log("infromación leida del QR")
    let component_name = componet_select
    console.log("Component name:", component_name)    
    identifier = identifier.split('.')
    console.log('Identifier:', identifier[0] == component_name[0])
   /*  if( component_name.includes('-')){
        component_name = component_name.split('-')
        component_name = component_name[0] + component_name[1]
    } */

    /* identifier = identifier.split('.')
    identifier = identifier[0] */
    console.log(component_name)
    console.log(lote_component + " " + identifier + " " + current_month_qr + " " + current_year_qr)
    expiration_date = new Date(current_year_qr, current_month_qr - 1)
    let today_date = new Date()
    var differenceMonth = getMonthDifference(expiration_date, today_date)
    console.log(differenceMonth)
    /* if(differenceMonth > 6){
        console.log("Entro a validación de caducidad")
        $('#substanceCadModal').modal('show')
    } else if(identifier != component_name) {
        $('#qrErrorModal').modal('show')
    } else {        
        $('#componentCheckModal').modal('hide')
        $('#containerModal').modal('show')
        init_setup_scanner(1) // inicializndo todo en falso
    } */

    if(identifier[0] != component_name[0] && identifier[1] != component_name[1]) {
        $('#qrErrorModal').modal('show')
    } else {        
        $('#improvedCheckModal').modal('hide')
        $('#improvedcontainerModal').modal('show')
        init_setup_scanner(1) // inicializndo todo en falso
    }
}

function validationQRPaitInformation(){
    console.log("infromación leida del QR")
    let component_name = componet_select
    console.log("Component name:", component_name)
    identifier = identifier.split('.')
    console.log('Identifier:', identifier)    
    /* if( component_name.includes('-')){
        component_name = component_name.split('-')
        component_name = component_name[0] + component_name[1]
    } */

    /* identifier = identifier.split('.')
    identifier = identifier[0] */
    console.log(component_name)
    console.log(lote_component + " " + identifier + " " + current_month_qr + " " + current_year_qr)
    let expiration_date = new Date(current_year_qr, current_month_qr - 1)
    let today_date = new Date()
    var differenceMonth = getMonthDifference(expiration_date, today_date)
    console.log(differenceMonth)
    /* if(identifier != component_name){
        $('#qrErrorModal').modal('show')
    } else if(differenceMonth > 6) {
        $('#substanceCadModal').modal('show')
    } else {
        console.log("Entro a verdadero")
        $('#componentCheckModal').modal('hide') 
        $('#codeReadModal').modal('show')
        init_setup_scanner(1) // inicializndo todo en falso
    } */

    if( identifier[0] != component_name[0] && identifier[1] != component_name[1]){
        $('#qrErrorModal').modal('show')
    } else {
        console.log("Entro a verdadero")
        $('#componentCheckModal').modal('hide') 
        $('#codeReadModal').modal('show')
        init_setup_scanner(1) // inicializndo todo en falso
    }
}



function tryAnother(){
    init_setup_scanner(2)
    $('#substanceCadModal').modal('hide')
}

function releasedSubstance(){
    $('#componentCheckModal').modal('hide')
    $('#ensureInfoModal').modal('hide')
    $('#authDepartModal').modal('show')
}

$('#workerValidationModal').on('show.bs.modal', () => {
    r = 7
})

$('#qrErrorModal').on('show.bs.modal', () => {
    const timer = 6000
    setTimeout(() => {
        $('#qrErrorModal').modal('hide')
        init_setup_scanner(2)
    }, timer)
})

function getMonthDifference(start_date, end_date){
    return (end_date.getMonth() - start_date.getMonth() + 12 * (end_date.getFullYear() - start_date.getFullYear()))
}

$(BarcodesScanner).on('scan', async function(e){
    
    n_data++;
    /* console.log(n_data + ") " + data_) */
    /* console.log(r) */
    if(r == 4){
        var payroll_number = data_.slice(data_.length - 3)
        payroll_number = parseInt(payroll_number)
        await get_worker_byPayNumber(payroll_number)
        var worker_info = response_data
        console.log("Respuesta recibida",response_data.rest)
        if(response_data.rest == 'SUCCESS'){
            console.log("Scan lis",list_MixProcess)
            list_MixProcess['name_worker'] = worker_info.record.name
            list_MixProcess['id_worker'] = worker_info.record.payroll_number
            list_MixProcess['t_start'] = new Date().toISOString()
            window.localStorage.setItem('mixProcess', JSON.stringify(list_MixProcess))
            init_setup_scanner(1) // inicializndo todo en falso
            /* var e = JSON.parse(sessionStorage.getItem('mixProcess'))
            console.log("ste es el jsonb",e) */
            $('#CredentialsModal').modal('hide')
            await get_nextid_proces()
            var next_id_proces = response_data
            window.localStorage.setItem('next_id', next_id_proces.next_id)
            console.log(next_id_proces)
            console.log("local: ",localStorage)
            window.location.href = '/OT_Detail'
            data_ = ""
        } else {
            $('#CredentialsModal').modal('hide')
            $('#errorModal').modal('show')
            data_ = ""
        }
    }
    
    if(r == 5){        
        console.log("Entra contenedor")
        var barcode_text = data_
        console.log(barcode_text)
        await get_validation_container(barcode_text)
        console.log(list_Container)
        var response = response_data
        console.log(response)
        if(response.rest == "SUCCESS"){
            if(response.response == true){
                struct_start_container["id_barcode"] = barcode_text
                console.log(struct_start_container)
                await post_container(struct_start_container)
                $('#codeReadModal').modal('hide')
                $('#paintContainerModal').modal('show')
                init_setup_scanner(1) // inicializndo todo en falso
                document.getElementById('barcode').innerText = `${substance_language.barcode_label} ${barcode_text}`
            } else {
                $('#barcodeEContModal').modal('show')
            }
        } else {
            console.log("No se puede comunicar con el servidor, favor de revisar que el programa servidor este en ejecución")
            $('#errorSConnectModal').modal('show')
        }
        data_ = ""
    }

    if(r == 6){
        document.getElementById('substance').textContent = ""
    }

    if( r == 7){
        const date = new Date()
        let id_container = localStorage.getItem('id_component')
        var payroll_number = data_.slice(data_.length - 3)
        payroll_number = parseInt(payroll_number)
        await get_worker_byPayNumber(payroll_number)
        var worker_info = response_data
        console.log("Respuesta recibida",response_data.rest)
        if(response_data.rest == 'SUCCESS'){
            var job_position = response_data.record.job_position
            if(job_position == 2){
                struct_realese_process['id_process'] = id_process_
                struct_realese_process['id_worker'] = payroll_number
                struct_realese_process['id_type_release'] = 1
                struct_realese_process['time_stamp'] = date.toISOString()
                struct_realese_process['id_component_tare'] = -1
                struct_realese_process['id_container'] = parseInt(id_container)
                await post_process_step_release(struct_realese_process)
                $('#workerValidationModal').modal('hide')
                $('#containerModal').modal('show')
                init_setup_scanner(1) // inicializndo todo en falso
            }
        } else {
            $('#CredentialsModal').modal('hide')
            $('#errorModal').modal('show')
            data_ = ""
        }
    }
    
    if( r == 8){
        const date = new Date()
        let id_container = localStorage.getItem('id_component')
        var payroll_number = data_.slice(data_.length - 3)
        payroll_number = parseInt(payroll_number)
        await get_worker_byPayNumber(payroll_number)
        var worker_info = response_data
        console.log("Respuesta recibida",response_data.rest)
        if(response_data.rest == 'SUCCESS'){
            var job_position = response_data.record.job_position
            console.log(job_position)
            if(job_position == 2){
                struct_realese_process['id_process'] = id_process_
                struct_realese_process['id_worker'] = payroll_number
                struct_realese_process['id_type_release'] = 2
                struct_realese_process['time_stamp'] = date.toISOString()
                struct_realese_process['id_component_tare'] = -1
                struct_realese_process['id_container'] = id_container
                await post_process_step_release(struct_realese_process)
                $('#workerValidationTLModal').modal('hide')
                $('#removeContModal').modal('show')
                init_setup_scanner(1) // inicializndo todo en falso
                
            } else {
                $('#errorTeamLModal').modal('show')
            }
        } else {
            $('#CredentialsModal').modal('hide')
            $('#errorModal').modal('show')
        }
        data_ = ""
    }

    if(r == 10){
        var payroll_number = data_.slice(data_.length - 3)
        payroll_number = parseInt(payroll_number)
        await get_worker_byPayNumber(payroll_number)
        var worker_info = response_data
        console.log("Respuesta recibida",response_data.rest)
        if(response_data.rest == 'SUCCESS'){
            $('#CredentialsZPLModal').modal('hide')
            window.location.href = `/zpl/containers_labels/${payroll_number}`
        } else {
            $('#CredentialsModal').modal('hide')
            $('#errorModal').modal('show')        
        }
        data_ = ""
    }

    if(qr_interception == 11){
        qr_ = data_.split(';')
        split_info_id = qr_[1].split('=')
        id_container = split_info_id[1]
        let code = qr_[4].split(':')
        color_code = code[1]
        id_process = qr_[0].split('-')
        id_process = parseInt(id_process[1])
        await get_machine_info()
        identifier_machine = identifie_response.record.id_in
        console.log(identifie_response)
        machine_id = qr_[0].slice(2,4)
        if(identifier_machine == machine_id){
            //AQUÍ VA LA VALIDACIÓN PARA OBTNER LA INFO DEL ZPL
            await get_container_by_id(id_container)
            console.log("Contenedor",identifie_response)
            barcode = identifie_response.record.id_barcode
            if(identifie_response.rest == "SUCCESS"){
                viscosity_improved = identifie_response.record.viscosity
                await get_color_by_color_code(color_code)
                color_improved = identifie_response.record.name
                console.log(identifie_response)
                id_color = identifie_response.record.id
                max_viscosity = identifie_response.record.max_viscosity
                min_viscosity = identifie_response.record.min_viscosity
                if(viscosity_improved > max_viscosity){
                    if(identifie_response.rest == "SUCCESS"){
                        color_name_label.textContent = color_improved
                        viscosity_label.textContent = viscosity_improved
                        $('#containerReadModal').modal('hide')
                        $('#infoMixModal').modal('show')
                    } else {
                        console.log("ERROR no se encuentra el color")
                        $('#colorErrorModal').modal('show')
                    }
                } else {
                    console.log("ERROR no se requiere el mejorado")
                    $('#viscosityErrorModal').modal('show')
                }
            } else {
                console.log("ERROR no se encuentra el contenedor")
                $('#errorContainerModal').modal('show')
            }
        } else {
            console.log("ERROR no encuentra el identificador")
            $('#machineIdModal').modal('show')
        }
    }

});

$('#removeContModal').on('show.bs.modal', () => {
    const timer = 4000
    setTimeout(() => {
        $('#removeContModal').modal('hide')        
        $('#successModal').modal('show')
    },timer)
})

$('#errorModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#errorModal').modal('hide')        
        window.location.reload()
    },timer)
})

$('#barcodeEContModal').on('show.bs.modal', () => {
    const timer = 5000
    setTimeout(() => {
        $('#barcodeEContModal').modal('hide')
    }, timer)
})

$('#errorSConnectModal').on('show.bs.modal', () => {
    const timer = 5000
    setTimeout(() => {
        $('#errorSConnectModal').modal('hide')
    }, timer)
})

$('#errorTeamLModal').on('show.bs.modal', () => {
    const timer = 5000
    setTimeout(() => {
        $('#errorTeamLModal').modal('hide')
    }, timer)
})