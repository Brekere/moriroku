let substance_name = undefined
let weight_container_limit = 12000

let label_operator_name = document.getElementById('OPName')
let label_lot_ = document.getElementById('lotname')
let label_work_order = document.getElementById('WorkO')
let label_date = document.getElementById('date')
let label_color_code = document.getElementById('colorcode')
let label_color_name = document.getElementById('colorname')
let label_conatiner_q = document.getElementById('containernumber')
let label_weight = document.getElementById('weight-container')
let label_barcode = document.getElementById('barcode_num')

const btn_index_Container = 0

let improvedCheckModal = document.getElementById('improvedCheckModal')
let btn_readySubstance = document.getElementById('readySubsatance')
let btn_readyCombinate = document.getElementById('readyCombination')

let improved_info = JSON.parse(localStorage.getItem('improved_info'))
let list_components = JSON.parse(localStorage.getItem('components_formula'))
let list_Container = JSON.parse(localStorage.getItem(`mixContainer-${btn_index_Container}`))
let id_component = parseInt(localStorage.getItem('id_component')) //ESTE ES EL ID DEL CONTENEDOR
let containers = parseInt(localStorage.getItem('num_containers'))
var actual_container = localStorage.getItem('actual_container')
var mixProcess = JSON.parse(localStorage.getItem('mixProcess'))
let initial_info_component = JSON.parse(localStorage.getItem('initial_info'))

list_improved_ = JSON.parse(list_improved_)

document.getElementById('color-name-improved').textContent = improved_info['color_name']
document.getElementById('barcode_num').textContent = improved_info['barcode']

label_barcode.textContent = improved_info['barcode']

const max_viscosity = improved_info['max_viscosity']
const min_viscosity = improved_info['min_viscosity']
const id_container = improved_info['id_container']
improved_info['id_component'] = list_improved_[0].id_component

var struct_info = {
    'id' : id_container,
    "viscosity": "",
    "weight": "",
    "humidity": "",
    "temperature": ""
}

var struct_info_improvement = {
    "id_mix_container" : improved_info['id_container'],
    "new_viscosity" : "",
    "id_component" : list_improved_[0].id_component,
    "extra_weight" : "", // gr_level de la sustancia que se esta virtiendo
    "t_start" : "",
    "t_end" : "",
    "batch" : ""
}

$(document).ready(() => {
    loadJSFilePrinter()
    loadImproveJSFile()
})

function startImproved(element){
    substance_name = element.value    
    btn_readyCombinate.style.display = 'none'
    let tolerance_sustance = list_improved_[0].tolerance/100
    init_values_improved(list_improved_[0].substance_g, weight_container_limit, tolerance_sustance)
    document.getElementById('substance').textContent = `${list_improved_[0].type_component} ${list_improved_[0].component_nickname}`
    $('#improvedcalinModal').modal('show')
    /* $('#timerImproveModal').modal('show') */
}

$("#improvedCheckModal").on('show.bs.modal', () => {
    init_setup_scanner(2)
    /* setTimeout(() => {
        $('#improvedCheckModal').modal('hide')
        $('#containerModal').modal('show')
    }, 4000) */
})

function readyBtn(){
    $('#improvedcontainerModal').modal('hide')
    $('#improvedcalinModal').modal('show')
}

async function checkSustance(btn_value){
    const timer = 4000
    const date = new Date()

    if(gr_level < gr_min_accept){
        document.getElementById('graphWarnModalLabel').textContent = `${improved_mix.level_min_modal_title}`
        document.getElementById('errorBody').textContent = `${improved_mix.level_min_modal_body}`
        $('#graphWarnModal').modal('show')
    } else {
        if(gr_level >= gr_min_accept && gr_level <= gr_max_accept){
            switch(btn_value){
                case 1:
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
                    list_Container.weight = 8789 //Cambiar a gr level
                    console.log("Ciclo terminado!!!");
                    $('#improvedsustModal').modal('hide')
                    $('#timerImproveModal').modal('show')
                    break;
            }
        } else {
            document.getElementById('graphWarnModalLabel').textContent = `${improved_mix.level_max_modal_title}`
            document.getElementById('errorBody').textContent = `${improved_mix.level_max_modal_body}`
            $('#graphWarnModal').modal('show')
        }
    }
}

$('#timerImproveModal').on('show.bs.modal', function(){    
    var sec = 20
    var timer = setInterval(function(){    
     document.getElementById('timerImprove').innerHTML = sec + " s"
     sec--
     if(sec < 0){
         clearInterval(timer)
         document.getElementById('btn-finish').style.display = 'inline'
         document.getElementById('btn-finish').focus()
     }
    }, 1000)
})

function addImproveTemperature(){
    const date = new Date()
    $('#timerImproveModal').modal('hide')
    $('#temperatureImproveModal').modal('show')
}

async function temperatureImproveAdd(){
    var date = new Date()
    let temperature = document.getElementById('temperature_id_0').value
    let humidity = document.getElementById('humidity_id_1').value
    let viscosity = document.getElementById('viscosity_id_2').value
    if(temperature != '' && humidity != '' && viscosity != ''){
        /*struct_info['humidity'] = humidity
        struct_info['temperature'] = temperature
        struct_info['viscosity'] = viscosity
        struct_info['weight'] = 9823 //Cambiar al peso total
        await post_container(struct_info) */        
        struct_info_improvement['extra_weight'] = 100
        struct_info_improvement['new_viscosity'] = parseFloat(viscosity)
        struct_info_improvement['batch'] = '025'
        struct_info_improvement['t_start'] = date.toISOString()
        struct_info_improvement['t_end'] = date.toISOString()
        await post_component_viscosity_improvement(struct_info_improvement)
        list_Container.rework = "RS"
        if(viscosity >= min_viscosity && viscosity <= max_viscosity){
            list_Container.rework = "RN"
            list_Container.t_end = date.toISOString()
            console.log(list_Container)
            paintInfoLabel()
            localStorage.setItem(`mixContainer-${btn_index_Container}`, JSON.stringify(list_Container))            
            setup()
            $('#temperatureImproveModal').modal('hide')
            $('#reportModal').modal('show')
        } else if(viscosity < min_viscosity){            
            list_Container.t_end = date.toISOString()
            console.log(list_Container)
            paintInfoLabel()
            localStorage.setItem(`mixContainer-${btn_index_Container}`, JSON.stringify(list_Container))            
            setup()
            paintWarningImprove(1, min_viscosity, max_viscosity, viscosity)
        } else if(viscosity > max_viscosity){
            list_Container.t_end = date.toISOString()
            console.log(list_Container)
            paintInfoLabel()
            localStorage.setItem(`mixContainer-${btn_index_Container}`, JSON.stringify(list_Container))            
            //setup()
            paintWarningImprove(1, min_viscosity, max_viscosity, viscosity)
        }        
    } else {
        $('#errorInfoModal').modal('show')
    }
}

function paintWarningImprove(value, min_visco, max_visco, visco){
    switch(value){
        case 1:
            document.getElementById('graphWarnPaintModalLabel').innerText = `${improved_mix.modal_warn_graph_title_min}`
            document.getElementById('errorPaintBody').innerText = `${improved_mix.modal_warn_graph_body_1} ${min_visco} - ${max_visco}. ${improved_mix.modal_warn_graph_body_2} ${visco}
            ${improved_mix.modal_warn_graph_body_min}`
            $('#temperatureImproveModal').modal('hide')
            $('#graphWarnPaintModal').modal('show')
            break;
        case 2:
            document.getElementById('graphWarnPaintModalLabel').innerText = `${improved_mix.modal_warn_graph_title_max}`
            document.getElementById('errorPaintBody').innerText = `${improved_mix.modal_warn_graph_body_1} ${min_visco} - ${max_visco}. ${improved_mix.modal_warn_graph_body_2} ${visco}
            ${improved_mix.modal_warn_graph_body_max}`
            $('#temperatureImproveModal').modal('hide')
            $('#graphWarnPaintModal').modal('show')
            break
    }
}

function paintInfoLabel(){
    label_operator_name.textContent = mixProcess['name_worker']
    label_lot_.textContent = initial_info_component['n_lote']
    label_work_order.textContent = initial_info_component['order_work']
    label_date.textContent = (new Date(struct_info_improvement['t_end']).toLocaleString()).replace(',', '')
    label_color_code.textContent = initial_info_component['color_code']
    label_color_name.textContent = initial_info_component['color_name']
    label_conatiner_q.textContent = actual_container
    let total_weight = 7262;
    label_weight.textContent = total_weight
    let html_label_components = document.getElementById('list-substances')
    for (let x = 0; x < list_components.length; x++) {
        if(list_components[x]['comp_name'] == list_improved_[0]['component_identifier']){
            list_components[x]['weight'] = list_components[x]['weight'] + 100 //cambiar por el gr_level de la báscular
        }
        html_label_components.innerHTML += `
        <h3><li>${list_components[x]['type_compent_name']} -- ${list_components[x]['comp_name']} -- w: ${list_components[x]['weight']}g</li></h3
        `
    }
}

$('#graphWarnModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(function(){
        $('#graphWarnModal').modal('hide')
    }, timer)
})

$('#graphWarnPaintModal').on('show.bs.modal', () => {
    const timer = 7000
    console.log("Entra")
    setTimeout(function(){
        $('#graphWarnPaintModal').modal('hide')
        
        $('#reportModal').modal('show')
    }, timer)
})


$('#improvedcalinModal').on('show.bs.modal', () => {
    const timer = 7000
    setTimeout(function(){
        $('#improvedcalinModal').modal('hide')
    }, timer)
})

$('#errorInfoModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorInfoModal').modal('hide')
    },5000)
})

$('#improvedCheckModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#improvedCheckModal').modal('hide')
        $('#improvedcontainerModal').modal('show')
    },7000)
})

function backPage() {
    window.location.replace('/')
}