/* var radio_btn = undefined
var btns = [] */
let e = undefined
let index_check_btn = 1
let btn_index_Container = parseInt(localStorage.getItem('chkId'))
let len_btn_Container = parseInt(localStorage.getItem('lenBtns'))
let list_Container = JSON.parse(localStorage.getItem(`mixContainer-${btn_index_Container}`))
mixProcess = JSON.parse(localStorage.getItem('mixProcess'))
let initial_info_component = JSON.parse(localStorage.getItem('initial_info'))
actual_container = localStorage.getItem('actual_container')
let id_component = parseInt(localStorage.getItem('id_component')) //ESTE ES EL ID DEL CONTENEDOR
var containers = parseInt(localStorage.getItem('num_containers'))
let weight_base = parseInt(localStorage.getItem('base_weigth'))
var JSON_list = JSON.parse(list_component)
var viscosity_obteined = ''

let data_component_base = {}
let index_btn = 0
let weight_Subs = 0
let expected_weight = 0
let weight_container_limit = 12000
let percent_Subs = 0
let index_title = 1
let index_weight = 0
let contaier_expected_weight = 0
let btn = undefined
let unit = undefined
let year = undefined
let month = undefined
let num_lot = undefined
let provider = undefined
let qr_weight = undefined
let componet_select = undefined
let id_component_base = undefined
var last_subs = undefined
let type_component = undefined
let batch_component_tare = undefined
const min_temp = 20.0
const max_temp = 24.0
const min_hum = 30.0
const max_hum = 70.0

document.getElementById(`container-count`).textContent = `${substance_language.title_container} ${index_title}/${list_json.length}`

var struct_start_container = {
    'id' : id_component,
    'id_barcode' : "",
    "t_start_container": ""
}

var struct_start_tare = {
    'id' : id_component,
    "t_start_tare" : ""
}

var struct_info = {
    'id' : id_component,
    "viscosity": "",
    "weight": "",
    "humidity": "",
    "temperature": ""
}

var struct_end_tare = {
    'id' : id_component,
    "t_end_tare": ""
}

var struct_end_container = {
    'id' : id_component,
    "t_end_container": ""
}

var struct_start_viscosity = {
    'id' : id_component,
    "t_start_viscosity": ""
}

var struct_end_viscosity = {
    'id' : id_component,
    "t_end_viscosity": ""
}

var struct_t_end = {
    'id' : id_component,
    "t_end": ""
}

struct_departament = {
    "departament": "",
    "password": ""
}

var struct_component_tare = {
    "id_mix_container" : "",
    "id_type_compoennt": "",
    "id_component": "",
    "weight" : "",
    "t_start" : "",
    "t_end" : "",
    "batch": "",
    "batch_expiration" : ""
}

btn = btns[index_btn]

$(document).ready(async () => { 
    loadJSFilePrinter()
    loadJSFile()
})

var btn_readyG = document.getElementById('readyGraphBtn')
var btn_readyG2 = document.getElementById('readyGraphBtn2')
var btn_readyG3 = document.getElementById('readyGraphBtn3')
var btn_init_tare = document.getElementById('initTareGraph2')

function update_levels_loop(){
    var ele = document.getElementById('fillLeves-container')
    get_weight(port_loop);
    draw_fill_levels_stacked_bar(ele.id);
}

var list_comp_formula = JSON.parse(localStorage.getItem('components_formula'))

function loadJSFilePrinter(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/BrowserPrint-3.0.216.min.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);

    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/BrowserPrint-Zebra-1.0.216.min.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);

    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/format_connection.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
  }

  function loadJSFile(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/scanner_connection/scanner.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
  }


async function eclick(element){
    //id_component_base = $(element).attr('data-item-id')
    var sub_name = element.value
    type_component = JSON_list.find(x => x.name_component == sub_name)
    document.getElementById('component').textContent = `${type_component['name_type']} ${type_component['nickname'].toString()}`
    console.log(sub_name)
    const date = new Date()
    id_component_ = parseInt($(element).attr('data-item-id'))
    /* var JSON_list = JSON.parse(list_component) */
    //var type_component = JSON_list.find(x => x.id_component == id_component_)
    struct_component_tare['id_component'] = id_component_
    struct_component_tare['id_mix_container'] = id_component
    struct_component_tare['id_type_compoennt'] = type_component['type']
    struct_component_tare['t_start'] = date.toISOString()
    
    data_component_base = {
        "id_type" : type_component['type'],
        "id_component" : parseInt(id_component_)
    }

    if(data_component_base["id_type"] == 2 && data_component_base["id_component"] == 0){
        console.log("Detecto caso especial")
        special_case_ln245 = true
    } else {
        console.log("Caso Normal")
        special_case_ln245 = false
    }
    
    contaier_expected_weight = weight_base * total_percent
    var tolerance = 0
    last_subs = list_json[list_json.length-1]['name_component']
    for (let index_js = 0; index_js < list_json.length; index_js++) {
        if(list_json[index_js]['name_component'] === element.value){
            tolerance = list_json[index_js]['tolerance']/100
            percent_Subs = list_json[index_js]['percent']
            index_js = list_json.length
            expected_weight = weight_base * percent_Subs /100
            break
        }
    }
    init_values_jug(expected_weight, weight_container_limit, tolerance)
    
    if(btn != btns[btns.length-1]){
        if(btn == btns[0]){
            struct_start_tare['t_start_tare'] = date.toISOString()
            console.log("Primero", struct_start_tare["t_start_tare"])
            await post_container(struct_start_tare)
        }
    }
    

    if(btn.value != last_subs){
        contenedor = false
        console.log(list_Container)
        componet_select = document.getElementById('component-list').textContent
        console.log('01:',componet_select)
        //document.getElementById('component').innerText = componet_select        
        $('#componentCheckModal').modal('show')
        document.getElementById('substance-tare').textContent = sub_name.toString()
        await get_component_identifier(data_component_base)        
        console.log("Respuesta:",identifie_response)
        if(identifie_response.rest == "SUCCESS"){
            identifie_response
            componet_select = (identifie_response.identifier).split('.')
            console.log('02:',componet_select)
            console.log(list_Container)
            btn_readyG2.style.display = 'inline'
            btn_readyG3.style.display = 'none'
        }
        btn_readyG2.style.display = 'none'
        btn_readyG3.style.display = 'none'
    } else {
        contenedor = true
        $('#componentCheckModal').modal('show')
        document.getElementById('substance_graph').textContent = sub_name.toString()
        await get_component_identifier(data_component_base)
        console.log("Respuesta:",identifie_response)
        if(identifie_response.rest == "SUCCESS"){
            console.log("Identificador",identifier)
            componet_select = identifie_response.identifier
            //document.getElementById('component').innerText = componet_select        
            console.log(list_Container)
            struct_start_container["t_start_container"] = date.toISOString()
            btn_readyG2.style.display = 'inline'
            btn_readyG3.style.display = 'none'
        } else {
            $('#qrErrorModal').modal()
        }
    } 
}

$('#componentCheckModal').on('show.bs.modal', () => {
    r = 6
    init_setup_scanner(2)
    /* const timer = 4000
    setTimeout(function(){
        $('#componentCheckModal').modal('hide')
        $('#codeReadModal').modal('show')
    }, timer) */
})
 
function readyBtn(){
    $('#containerModal').modal('hide')
    $('#calibrationModal').modal('show')
}

$('#calibrationModal').on('shown.bs.modal', function() {
    if(response_tare) {
        const timer = 4000
        setTimeout(function(){
            $('#calibrationModal').modal('hide')
            $('#sustModal').modal('show')
        },timer)
    }
})

$('#errorTareModal').on('show.bs.modal', () => {
    var sec = 10
    var timer = setInterval(function(){
     sec--
     if(sec < 0){
         clearInterval(timer)
         localStorage.clear()
         window.location.href = '/'
     }
    }, 1000)
})

function liberationOfSmallWeight(){
    let gr_expected_truncate = Math.trunc((gr_min_accept + gr_max_accept) / 2)
    let error_gr_expected = (gr_min_accept - gr_max_accept) / 2
   let dif_gr_level_expected = Math.abs(gr_expected_truncate - gr_level)

    console.log(gr_expected_truncate)
    console.log(error_gr_expected)
    console.log(dif_gr_level_expected)

    /* gr_expected_truncate % 2 == 1 && error_gr_expected < 1 && dif_gr_level_expected < 1.5 */
    if(Math.trunc(gr_max_accept) % 2 == 1 && error_gr_expected < 1 && dif_gr_level_expected < 1.5){
        console.log("Entro")
        return true
    } else {
        return false
    }
}

function checkMix(){
    if(gr_level < gr_min_accept){
        var response_function = liberationOfSmallWeight()
        console.log(response_function)
        if(response_function == false){
            document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Abajo'
            document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de bajo del promedio. Favor de vertir más sustancia.'
            $('#graphWarnModal').modal('show')
        }else {
            $('#grLevelLibeModal').modal('show')
        }
    } else {
        if(gr_level >= gr_min_accept && gr_level <= gr_max_accept){
            clearInterval(refreshIntervalId_update_weight);
                loop_w = false;
                port_loop = "";
                refreshIntervalId_update_weight = null;
                console.log("Ciclo terminado!!!");
                $('#sustModal').modal('hide')
                $('#removeContModal').modal('show')
            } else {
                var response_function = liberationOfSmallWeight()
                if(response_function == false) {
                    document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Encima'
                    document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de encima del promedio. Favor de quitar sustancia.'
                    $('#graphWarnModal').modal('show')
                } else {
                    $('#grLevelLibeModal').modal('show')
                }
            }
        }
}

$('#removeContModal').on('show.bs.modal', () => {
    const timer = 3000
    setTimeout(() => {
        $('#removeContModal').modal('hide')
        $('#successModal').modal('show')
    }, timer)
})
     
$('#successModal').on('show.bs.modal', async () => {
    const date = new Date()
    struct_component_tare['t_end'] = date.toISOString()
    struct_component_tare['weight'] = gr_level
    struct_component_tare['batch'] = batch_component_tare
    struct_component_tare['batch_expiration'] = expiration_date.toISOString()
    console.log("componente lista tare: ",struct_component_tare)
    await post_component_tare(struct_component_tare)
    setTimeout(() => {
        $('#successModal').modal('hide')
    }, 3500)
        
    paintWeight(1)
        
    if(btn == btns[btns.length-2] && btn != undefined){
        struct_end_tare["t_end_tare"] = date.toISOString()
        console.log("Last Oner",struct_end_tare["t_end_tare"])
        await post_container(struct_end_tare)
    } 
    btn.style.display = 'none'
    radio_btn[index_btn].checked = true
    index_btn++
    btn = btns[index_btn]
    btn.style.display = 'inline'
})

function paintWeight(value){
    switch(value){
        case 1:
            var weight = gr_level
            weight_Subs += weight
            document.getElementById(`weight-${index_weight}`).textContent = `${weight.toFixed(0)} g`
            document.getElementById(`container-count`).textContent = `${substance_language.title_container} ${index_title+1}/${list_json.length}`
            document.getElementById(`weigth-total`).textContent = `${weight_Subs.toFixed(0)} g`
            console.log( `Expected: ${contaier_expected_weight} y Sumatoria: ${weight_Subs} ==> ${((expected_weight/weight_Subs)*100).toFixed(2)}`)
            document.getElementById('percent').textContent = `${((weight_Subs/contaier_expected_weight)*100).toFixed(2)} %`
            list_comp_formula[index_btn]['weight'] = weight.toFixed(0)
            console.log(list_comp_formula[index_btn]['weight'])
            console.log(list_comp_formula)
            index_weight = index_weight + 1
            break;    
        case 2:
            var weight = gr_level
            weight_Subs += weight
            document.getElementById(`weight-${index_weight}`).textContent = `${weight.toFixed(0)} g`
            document.getElementById(`container-count`).textContent = `${substance_language.title_container} ${index_title+1}/${list_json.length}`
            document.getElementById(`weigth-total`).textContent = `${weight_Subs} g`
            document.getElementById('percent').textContent = `${((weight_Subs/contaier_expected_weight)*100).toFixed(2)} %`            
            list_comp_formula[index_btn]['weight'] = weight.toFixed(0)
            console.log("Lista final:",list_comp_formula)
            break;
    }
}


/* PROCESO DE LLENADO DEL CONTENEDOR */ 

$('#codeReadModal').on('show.bs.modal', () => {
    r=5
    /* setTimeout(() => {
        $('#codeReadModal').modal('hide')        
        $('#paintContainerModal').modal('show')        
    }, 3000) */
})

function readyPaintBtn(){
    $('#paintContainerModal').modal('hide')
    $('#paintCalibrationModal').modal('show')
}


$('#paintCalibrationModal').on('shown.bs.modal', function() {
    const timer = 4000
    setTimeout(function(){
        $('#paintCalibrationModal').modal('hide')
        $('#sustMixModal').modal('show')
    },timer)
})



async function readyMix(btn_value){
    const timer = 4000
    const date = new Date()

    if(gr_level < gr_min_accept){
        liberationOfSmallWeight()
        document.getElementById('graphWarnModalLabel').textContent = `${substance_language.level_min_modal_title}`
        document.getElementById('errorBody').textContent = `${substance_language.level_min_modal_body}`
        $('#graphWarnModal').modal('show')
    } else {
        if(gr_level >= gr_min_accept && gr_level <= gr_max_accept){   
            switch(btn_value){
                case 1:
                    struct_component_tare['weight'] = gr_level
                    $('#successPaintModal').modal('show')
                    $('#successPaintModal').on('shown.bs.modal', () => {
                        setInterval(function(){
                            btn_readyG2.style.display = 'none'
                            btn_init_tare.style.display = 'none'
                            btn_readyG3.style.display = 'inline'
                            $('#successPaintModal').modal('hide')
                        }, timer)
                    })
                    paintWeight(2)
                    clearInterval(refreshIntervalId_update_weight);
                    init_values_container(contaier_expected_weight, weight_container_limit, .005)
                    refreshIntervalId_update_weight = setInterval(update_levels_loop, time_interval_ms)
                    btn.style.display = 'none'
                    radio_btn[index_btn].checked = true
                    struct_component_tare['t_end'] = date.toISOString()
                    struct_component_tare['batch'] = batch_component_tare
                    console.log("componente lista tare: ",struct_component_tare)
                    await post_component_tare(struct_component_tare)
                    break;
                case 2:                    
                    clearInterval(refreshIntervalId_update_weight);
                    refreshIntervalId_update_weight = null;
                    console.log("Ciclo terminado!!!");
                    $('#sustMixModal').modal('hide')
                    $('#timerModal').modal('show')
                    weight_Subs = gr_level
                    break
            }      
                     
        } else {
            liberationOfSmallWeight
            document.getElementById('graphWarnModalLabel').textContent = `${substance_language.level_max_modal_title}`
            document.getElementById('errorBody').textContent = `${substance_language.level_max_modal_body}`
            $('#graphWarnModal').modal('show')
        }
    }
}

$('#timerModal').on('shown.bs.modal', function(){
    var sec = 20
    var timer = setInterval(function(){    
     document.getElementById('timer').innerHTML = sec + " s"
     sec--
     if(sec < 0){
         clearInterval(timer)
         document.getElementById('btn-finish').style.display = 'inline'
         document.getElementById('btn-finish').focus()
     }
    }, 1000)
 })
 
async function addTemperature(){
    const date = new Date()
    struct_start_viscosity['t_start_viscosity'] = date.toISOString()    
    await post_container(struct_start_viscosity)
     $('#timerModal').modal('hide')
     $('#temperatureModal').modal('show')
}

function showComponents(){
    console.log(components_by_formula)
    for (let index = 0; index < list_comp_formula.length; index++) {
        document.getElementById('list-substances').innerHTML += `
            <h3><li>${list_comp_formula[index]['type_compent_name'][0]} -- ${list_comp_formula[index]['comp_name']} -- w: ${list_comp_formula[index]['weight']}g</li></h3
        `
    }
}

async function temperatureAdded(){
    var date = new Date()
    const min_visco = mixProcess.expected_viscosity_min
    const max_visco = mixProcess.expected_viscosity_max
    list_Container.t_start_viscosity = date.toISOString()
    var temp = document.getElementById('temperature_id_0').value
    var hum = document.getElementById('humidity_id_1').value
    viscosity_obteined = document.getElementById('viscosity_id_2').value
    list_Container.humidity = hum
    list_Container.temperature = temp
    if(temp != '' && hum != '' && viscosity_obteined != ''){
        struct_info['humidity'] = parseFloat(hum)
        struct_info['temperature'] = parseFloat(temp)
        struct_info['viscosity'] = parseFloat(viscosity_obteined)
        struct_info['weight'] = parseInt(weight_Subs)
        await post_container(struct_info)
        response_limits = checkLimits(struct_info['humidity'], struct_info['temperature'])
        if(response_limits == null){
            list_Container.rework = "RS"
            if(viscosity_obteined >= min_visco && viscosity_obteined <= max_visco){
                await paintLabel(0, viscosity_obteined)
                $('#reportModal').modal('show')
                $('#temperatureModal').modal('hide')
            } else if( viscosity_obteined < min_visco){
                await paintLabel(1, viscosity_obteined)
                paintWarningVisco(1, min_visco, max_visco, viscosity_obteined)
            } else if(viscosity_obteined > max_visco){
                await paintLabel(1, viscosity_obteined)
                paintWarningVisco(2, min_visco, max_visco, viscosity_obteined)
            }
        } else {
            switch(response_limits){
                case "humidity":
                    console.log("Humedad fuera del limite")
                    struct_error_container['failed_process'] = true
                    struct_error_container['failure_type'] = 1
                    struct_error_process['failed_process'] = true
                    struct_error_process['failure_type'] = 1
                    struct_error_process['failure_description'] = "Humedad fuera del rango permitido"
                    $('#temperatureModal').modal('hide')
                    $('#humLimitsModal').modal('show')
                    break
                case "temperature":
                    console.log("Temperatura fuera del limite")
                    struct_error_container['failed_process'] = true
                    struct_error_container['failure_type'] = 0
                    struct_error_process['failed_process'] = true
                    struct_error_process['failure_type'] = 0
                    struct_error_process['failure_description'] = "Temperatura fuera del rango permitido"
                    $('#temperatureModal').modal('hide')
                    $('#tempLimitsModal').modal('show')
                    break
                case "both":
                    console.log("Temperatura y humedad fuera del limite")
                    struct_error_container['failed_process'] = true
                    struct_error_container['failure_type'] = 2
                    struct_error_process['failed_process'] = true
                    struct_error_process['failure_type'] = 2
                    struct_error_process['failure_description'] = "Humedad y temperatura fuera del rango permitido"
                    $('#temperatureModal').modal('hide')
                    $('#bothLimitsModal').modal('show')
                    break
                default:
                    console.log("Error")
                    break
            }
        }
    } else {
        $('#errorInfoModal').modal('show')
    }
}

function checkLimits(_humidity, _temperature){
    if(_temperature >= min_temp && _temperature <= max_temp && _humidity >= min_hum && _humidity <= max_hum){
        return null
    } else if(_temperature < min_temp){
      if(_humidity < min_hum || _humidity > max_hum){
        console.log("Temperatura y humedad fuera del limite")
        return 'both'
      } else {
        console.log("Temperatura fuera del limite")
        return 'temperature'
      }
    } else if(_temperature > max_temp) {
      if(_humidity < min_hum || _humidity > max_hum){
        console.log("Temperatura y humedad fuera del limite")
        return "both"
      } else {
        console.log("Temperatura fuera del limite")
        return 'temperature'
      }
    } else if(_humidity > max_hum) {
      if(_temperature < min_temp && _temperature > max_temp){
        console.log("Temperatura y humedad fuera del limite")
        return "both"
      } else {
        console.log("Humedad fuera del limite")
        return 'humidity'
      }
    } else if(_humidity < min_hum) {
      if(_temperature < min_temp && _temperature > max_temp){
        console.log("Temperatura y humedad fuera del limite")
        return "both"
      } else {
        console.log("Humedad fuera del limite")
        return 'humidity'
      }
    }
}

async function paintLabel(error, viscosity_obteined){
    const date = new Date()
    list_Container.viscosity = parseFloat(viscosity_obteined)
    list_Container.t_end_container = date.toISOString()
    list_Container.t_end_viscosity = date.toISOString()
    list_Container.t_end = date.toISOString()
    struct_t_end['t_end'] = date.toISOString()
    struct_end_container['t_end_container'] = date.toISOString()
    struct_end_viscosity['t_end_viscosity'] = date.toISOString()
    await post_container(struct_end_container)
    await post_container(struct_end_viscosity)
    await post_container(struct_t_end)
    list_Container.id_barcode = 25874891
    list_Container.weight = parseFloat(weight_Subs)
    console.log(list_Container)
    var array_name = mixProcess.name_worker.split(" ")
    var name = array_name[0] + " " + array_name[1]
    document.getElementById('OPName').textContent = name
    document.getElementById('lotname').textContent = initial_info_component.n_lote
    document.getElementById('WorkO').textContent = initial_info_component.order_work
    var local_date = new Date(list_Container.t_start)
    document.getElementById('date').textContent = local_date.toLocaleString()
    document.getElementById('colorcode').textContent = initial_info_component.color_code
    document.getElementById('colorname').textContent = initial_info_component.color_name
    document.getElementById('containernumber').textContent = `${actual_container}/${containers}`
    document.getElementById('weight-container').textContent = list_Container.weight
    showComponents()
    localStorage.setItem(`mixContainer-${btn_index_Container}`, JSON.stringify(list_Container))
    localStorage.setItem('components_formula', JSON.stringify(list_comp_formula))
    setup()
    if(error == 0){
        list_Container.rework = "RN"
    }
}

function paintWarningVisco(value, min_visco, max_visco, visco){
    switch(value){
        case 1:
            document.getElementById('graphWarnPaintModalLabel').innerText = 'Viscosidad Por Debajo del Rango'
            document.getElementById('errorPaintBody').innerText = `El rango de viscosidad de la mezcla es entre ${min_visco} - ${max_visco}. La viscosidad obtenida ${visco}
            esta por debajo del rango. Favor de mejorar la mezcla fuera del sistema actual.`
            $('#temperatureModal').modal('hide')
            $('#graphWarnPaintModal').modal('show')
            break;
        case 2:
            document.getElementById('graphWarnPaintModalLabel').innerText = 'Viscosidad Por Encima del Rango'
            document.getElementById('errorPaintBody').innerText = `El rango de viscosidad de la mezcla es entre ${min_visco} - ${max_visco}. La viscosidad obtenida ${visco}
            esta por encima del rango. Favor de mejorar la mezcla fuera del sistema actual.`
            $('#temperatureModal').modal('hide')
            $('#graphWarnPaintModal').modal('show')
            break
    }
}

$('#graphWarnPaintModal').on('show.bs.modal', () => {
    const timer = 7000
    setup()
    setTimeout(() => {
        $('#graphWarnPaintModal').modal('hide')
        $('#reportModal').modal('show')
    }, timer)
})

$('#errorInfoModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#errorInfoModal').modal('hide')
    }, timer)
    $('#reportModa').modal('show')
})

$('#graphWarnModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(function(){
        $('#graphWarnModal').modal('hide')
    }, timer)
})

async function authDepartament(){
    let password = document.getElementById('pass').value
    let departament_list = document.getElementById('select-form-departament')
    let departament = departament_list.options[departament_list.selectedIndex].label
    if(password != "" && departament != ""){
      struct_departament['departament'] = departament
      struct_departament['password'] = password
      await post_auth_departament(struct_departament)
      var response = api_response
      console.log(response.data.rest)
      if(response.data.rest == "SUCCESS") {
        $('#authDepartModal').modal('hide')
        $('#containerModal').modal('show')
      } else {
        $('#errorModal').modal('show')
      }
    } else {
        $('#errorAthModal').modal('show')
    }
}

/* $('#adjustviscoModal').on('shown.bs.modal', function() {
    var date = new Date()
    const timer = 7000
    const viscosity = 6
    var viscosity_obteined = parseInt(document.getElementById('visco').value)
    if (viscosity_obteined = viscosity){
        list_Container.viscosity = viscosity_obteined
        list_Container.t_end_viscosity = date.toISOString()
       $('#viscosityModal').modal('hide')
       $('#reportModa').modal('show')
   }
})
 */

function backPage() {
    if(btn_index_Container > 0){        
        localStorage.setItem('chkId', (btn_index_Container -1))
        window.location.replace('/mixing/containers/')
    } else if(btn_index_Container == 0){
        localStorage.removeItem('chkId')
        window.location.replace('/mixing/containers/')
    }
}

/* $('#exampleModal').on('show.bs.modal', () => {
    setup()
}) */

function backGraph() {
    $('#grLevelLibeModal').modal('hide')
}

function release(){
    clearInterval(refreshIntervalId_update_weight);
    $('#sustModal').modal('hide')
    $('#workerValidationTLModal').modal('show')
}

$('#workerValidationTLModal').on('show.bs.modal', () => {
    r = 8
})

$('#errorAthModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#errorAthModal').modal('hide')
    }, timer)
})

function examplePaint(value){
    $('#removeContModal').modal('show')
}

$('#tempLimitsModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#tempLimitsModal').modal('hide')
        $('#credentialsAssistantModal').modal('show')
    }, timer)
})

$('#humLimitsModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#humLimitsModal').modal('hide')
        $('#credentialsAssistantModal').modal('show')
    }, timer)
})

$('#bothLimitsModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(() => {
        $('#bothLimitsModal').modal('hide')
        $('#credentialsAssistantModal').modal('show')
    }, timer)
})

$('#credentialsAssistantModal').on('show.bs.modal', () => {
    r = 15
})
