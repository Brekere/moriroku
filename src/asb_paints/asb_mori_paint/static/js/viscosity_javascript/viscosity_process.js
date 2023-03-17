let barcode = undefined
let id_color = undefined
let id_process = undefined
let color_code = undefined
let id_container = undefined
let color_improved = undefined
let viscosity_improved = undefined
let identifier_machine = undefined
let max_viscosity = undefined
let min_viscosity = undefined

let rw_ = undefined

let improved_info = {
    "id_component": "",
    "id_color": "",
    "id_process": "",
    "barcode": "",
    "color_code": "",
    "color_name": "",
    "id_container": "",
    "viscosity_improved": "",
    "identifie_machine": "",
    "max_viscosity": "",
    "min_viscosity": ""
}

var initial_info = {
    "client_name" : "",
    "n_lote" : "",
    "order_work": "",
    "color_name": "",
    "color_code": "",
    "model": ""
}

var mixProcess = {
    "id_worker": "",
    "name_worker": ""
}

list_Container = {    
    "weight" : "",
    "t_end" : "",
    "rework" : ""
}

function loadJSFile(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "static/js/scanner_connection/scanner.js");
    
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
  }

let color_name_label = document.getElementById('color-name-improved')
let viscosity_label = document.getElementById('viscosity_improved')
let btn_start_improvement = document.getElementById('improvementS')
let qr_code_label = "L=M1-0000006;b=11;f=2022-07-18T17:46:06.707Z;e=191;c:7N5;w=7178g;m=2GJ.858.415.003;r=RS;i=Solvente,90186.0000.0.556,3186gbase,4611M.53LN.1.556,3982g"
//FALTA AGREGAR EN CODIGO ZPL EL VALOR DE b (b = ID DEL CONTENDOR)

/* $('#viscosityModal').on('show.bs.modal', async () => {
    loadJSFile()
    qr_ = qr_code_label.split(';')
    split_info_id = qr_[1].split('=')
    rw_ = qr_[7].split('=')
    rw_ = rw_[1]
    if(rw_ == "RS") {
        id_container = split_info_id[1]
        let code = qr_[4].split(':')
        color_code = code[1]
        id_process = qr_[0].split('-')
        id_process = parseInt(id_process[1])
        await get_container_by_id(id_container)
        barcode = identifie_response.record.id_barcode
        console.log(identifie_response)
        if(identifie_response.rest == "SUCCESS"){
            viscosity_improved = identifie_response.record.viscosity
            await get_color_by_color_code(color_code)
            color_improved = identifie_response.record.name
            console.log(identifie_response)
            id_color = identifie_response.record.id
            if(identifie_response.rest == "SUCCESS"){
                await get_machine_info()
                identifier_machine = identifie_response.record.id_in
                console.log(identifie_response)
                if(identifie_response.rest == "SUCCESS"){
                    setTimeout(() => {
                        $('#viscosityModal').modal('hide')
                        $('#containerReadModal').modal('show')
                    },5000)
                } else {
                    console.log("ERROR no encuentra el identificador")
                    $('#machineIdModal').modal('show')
                }
            } else {
                console.log("ERROR no se encuentra el color")
                $('#colorErrorModal').modal('show')
            }
        } else {
            console.log("ERROR no se encuentra el contenedor")
            $('#errorContainerModal').modal('show')
        }
    } else {
        console.log("ERROR la etiqueta no necesita rework")
        $('#reworkErrorModal').modal('show')
    }
}) */

$('#viscosityModal').on('show.bs.modal', async () => {
    loadJSFile()
    qr_ = qr_code_label.split(';')
    split_info_id = qr_[1].split('=')
    rw_ = qr_[7].split('=')
    rw_ = rw_[1]
    if(rw_ == "RS") {
        id_container = split_info_id[1]
        localStorage.setItem('id_component', id_container)
        let code = qr_[4].split(':')
        color_code = code[1]
        id_process = qr_[0].split('-')
        initial_info['n_lote'] = id_process[1]
        id_process = parseInt(id_process[1])
        await get_machine_info()
        identifier_machine = identifie_response.record.id_in
        console.log(identifie_response)
        machine_id = qr_[0].slice(2,4)
        if(identifier_machine == machine_id){
            await get_container_by_id(id_container)
            console.log("Contenedor",identifie_response)
            barcode = identifie_response.record.id_barcode
            if(identifie_response.rest == "SUCCESS"){
                viscosity_improved = identifie_response.record.viscosity
                await get_color_by_color_code(color_code)
                color_improved = identifie_response.record.name
                initial_info['color_name'] = color_improved
                initial_info['color_code'] = identifie_response.record.color_code
                console.log(identifie_response)
                id_color = identifie_response.record.id
                max_viscosity = identifie_response.record.max_viscosity
                min_viscosity = identifie_response.record.min_viscosity
                if(viscosity_improved > max_viscosity){
                    if(identifie_response.rest == "SUCCESS"){
                        setTimeout(() => {
                            $('#viscosityModal').modal('hide')
                            $('#containerReadModal').modal('show')
                        },5000)
                    } else {
                        console.log("ERROR no se encuentra el color")
                        $('#colorErrorModal').modal('show')
                    }
                }else{
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
    } else {
        console.log("ERROR la etiqueta no necesita rework")
        $('#reworkErrorModal').modal('show')
    }
})

$('#containerReadModal').on('show.bs.modal', () => {
    color_name_label.textContent = color_improved
    viscosity_label.textContent = viscosity_improved
    improved_info['color_code'] = color_code
    improved_info['color_name'] = color_improved,
    improved_info['barcode'] = barcode
    improved_info['id_color'] = id_color
    improved_info['id_container'] = parseInt(id_container)
    improved_info['id_process'] = id_process
    improved_info['identifie_machine'] = identifier_machine
    improved_info['viscosity_improved'] = viscosity_improved
    improved_info['max_viscosity'] = max_viscosity
    improved_info['min_viscosity'] = min_viscosity
    localStorage.setItem('improved_info',JSON.stringify(improved_info))
    console.log(improved_info)    
    setTimeout(() => {
        $('#containerReadModal').modal('hide')
        $('#infoMixModal').modal('show')
    },5000)
})

btn_start_improvement.addEventListener('click',async () => {
    qr_ = qr_code_label.split(';')
    machine_id = qr_[0].slice(2,4)
    await get_components_by_colorid(id_container)
    var response = identifie_response
    console.log(response.record)    
    localStorage.setItem("components_formula" ,JSON.stringify(response.record))
    if(identifie_response.rest == "SUCCESS") {
        id_process = parseInt(id_process)
        await get_process_by_id(id_process)
        var response = identifie_response
        console.log("Process ", response)
        if(identifie_response.rest == "SUCCESS") {
            let id_model = response.record.id_model
            let wo = response.record.work_order
            initial_info['order_work'] = wo
            await get_model_by_id(id_model)
            var response = identifie_response
            console.log(response)
            initial_info['model'] = response.model_name
            if(identifie_response.rest == "SUCCESS") {
                await get_zpl_info_by_id(id_container)
                let response = identifie_response
                console.log("ZPL ",response)
                mixProcess['id_worker'] = response.record.id_worker
                mixProcess['name_worker'] = response.record.name_worker
                initial_info['client_name'] = response.record.client_name
                localStorage.setItem('mixProcess', JSON.stringify(mixProcess))
                localStorage.setItem('actual_container', response.record.container)
                localStorage.setItem('num_containers', response.record.container_len)
                localStorage.setItem('mixContainer-0', JSON.stringify(list_Container))
                localStorage.setItem('initial_info', JSON.stringify(initial_info))
                window.location.href = `/viscosity/container/${id_color}`
            } else {

            }
        } else {

        }
    } else {
        $("#errorContainerModal").modal('show')
    }
})

$('#machineIdModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#machineIdModal').modal('hide')
        window.location.reload()
    },6000)
})

$('#containerErrorModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#containerErrorModal').modal('hide')
        window.location.reload()
    }, 6000)
})

$('#errorContainerModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorContainerModal').modal('hide')
        window.location.reload()
    }, 6000)
})

$('#reworkErrorModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#reworkErrorModal').modal('hide')
        window.location.reload()
    }, 6000)
})

$('#viscosityErrorModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#viscosityErrorModal').modal('hide')
        window.location.reload()
    }, 6000)
})