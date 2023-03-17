var index = '1'
var pieces = 0
var WO = ''
var id_formula = 0

var id_btn_prin = 0

var data_option_color = undefined
var model = undefined
var client_name = undefined
var lote = undefined
var wo = undefined
var baseWeight = undefined
var filter = undefined
let filter_model = undefined
const page = document.documentElement
var error_index = -1
let init_info_storage = undefined

var process_id = localStorage.getItem('next_id')
let select_model = document.getElementById('select-form-models')
let result_fullpage = localStorage.getItem('full_screen')
let btn_continue = document.getElementById('continue')

let btn = document.querySelector('#full')
var colors = []
var model = []
var filter = []

let list_MixProcess = JSON.parse(localStorage.getItem('mixProcess'))

const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

var d = new Date()
var date = d.getDate() + '/' + months[d.getMonth()] + '/' + d.getFullYear()
var time = (d.getHours() + '').padStart(2, '0') + ':' + (d.getMinutes() + '').padStart(2, '0') + ':' + (d.getSeconds() + '').padStart(2,'0')
var datetime = date + " " + time


document.getElementById('datetime').innerHTML = datetime

$(document).ready(() => {
    if(localStorage.getItem('initial_info') != null){
        console.log("Entra y hay algo en initial info")
        init_info_storage = JSON.parse(localStorage.getItem('initial_info'))
        btn_continue.style.display = 'inline'
        document.getElementById('add-WorkOrder').disabled = true
        document.getElementById('add-Pieces').disabled = true
        document.getElementById('select-form-color').disabled = true
        document.getElementById('select-form-models').disabled = true
        document.getElementById('checkInfo').style.display = 'none'
        document.getElementById('continue').style.display = 'inline'
        paintStorageValue(init_info_storage, list_MixProcess)
    }
})

function paintStorageValue(element_init_value, element_mixprocess_storage) {
    document.getElementById('input-area-0').value = element_init_value.order_work
    document.getElementById('input-area-1').value = element_mixprocess_storage.number_of_pieces
    document.getElementById('select-form-color').value = element_mixprocess_storage.id_formula
    document.getElementById('select-form-models').innerHTML = `<option selected value="0">${element_init_value.model}</option>`
    document.getElementById('filter').innerText = element_init_value.filter
}

/* document.getElementById('add-WorkOrder').focus()

var start_btn = document.getElementById('add-WorkOrder').focus() */

document.getElementById('lotName').innerText = (process_id + '').padStart(7, '0')

var initial_info = {
    "client_name" : document.getElementById('client_name').textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim(),
    "n_lote" : document.getElementById('lotName').textContent,
    "order_work": "",
    "color_name": "",
    "color_code": "",
    "model": "",
    "filter": ""
}
color_model = JSON.parse(color_model)

list_model = JSON.parse(models_list)

function filterSelect(element, list){
    if(element.value != -1){
        var len_selected = select_model.length
        for (let index = len_selected-1; index >= 0; index--) {
            select_model.remove(index)
        }
        list_MixProcess.id_formula = element.value
        var decode_Json = JSON.parse(list)
        console.log(decode_Json)
        var data_filter = decode_Json.find(x => x.id_formula == element.value)
        console.log(data_filter['color_code'])
        var name_filter = data_filter['name_filtro']
        var min_viscosity = data_filter['min_viscosity']
        var max_viscosity = data_filter['max_viscosity']   
        initial_info['color_code'] = data_filter['color_code']
        initial_info['color_name'] = data_filter['name_formula']
        console.log(initial_info)
        list_MixProcess.id_filter = data_filter['id_filtro']
        list_MixProcess.expected_viscosity_min = min_viscosity
        list_MixProcess.expected_viscosity_max = max_viscosity
        list_MixProcess.id_formula = parseInt(element.value)
        document.getElementById('filter').style.display = 'inline'
        document.getElementById('filter').textContent = name_filter
        initial_info['filter'] = name_filter
        console.log(list_MixProcess)
        filter_model = filterModelByColor(element.value)    
        console.log(filter_model)    
        select_model.disabled = false
        select_model.innerHTML += `<option selected value="0" id="select-opt-ph">${place_holder.textContent}</option>`
        for (let index = 0; index < filter_model.length; index++) {
            select_model.innerHTML += `                
                <option id="${filter_model[index]['id']}"> ${filter_model[index]['part_number']} </option>
            `
        }
        var data = document.getElementById('select-form-color')
        id_formula = data.options[data.selectedIndex].value
        error_index = id_formula
    } else {
        error_index = -1
        select_model.innerHTML += '<option selected value="0">Seleccionar...</option>'
        for (let index = 0; index < filter_model.length; index++) {
            select_model.remove(filter_model[index])
        }
        select_model.disabled = true        
    }
}

function filterModelByColor(id_color){
    let list_models = []
    let model_by_color = color_model.filter(x => x.id_color == id_color)
    for (let x = 0; x < list_model.length; x++) {
        for (let j = 0; j < model_by_color.length; j++) {
            if(list_model[x]['id']  == model_by_color[j]['id_model']){
                list_models.push(list_model[x])
            }
        }
    }
    return list_models
}

function modelSelect(){
    var data = document.getElementById('select-form-models')
    var model = data.options[data.selectedIndex].value 
    initial_info['model'] = model
    list_MixProcess.id_model = parseInt(data.options[data.selectedIndex].id)
    console.log(list_MixProcess)
    console.log(initial_info)
}

$('#checkInfo').click(() => {
    WO = document.getElementById('input-area-0').value
    pieces = document.getElementById('input-area-1').value
    list_MixProcess.work_order = WO
    var model_check = document.getElementById('select-form-models').value
    if(WO != '' && pieces != '' && error_index != -1 && model_check != 0 ){
        data_option_color = document.getElementById('select-form-color')
        color_formula = data_option_color[data_option_color.selectedIndex].text
        data_option_model = document.getElementById('select-form-models')
        model = data_option_model[data_option_model.selectedIndex].value    
        client_name = document.getElementById('client_name').textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim()
        lote = document.getElementById('lotName').textContent
        wo = document.getElementById('input-area-0').value
        pieces = document.getElementById('input-area-1').value
        //baseWeight = document.getElementById('baseWeight').value
        filter = document.getElementById('filter').textContent
        document.getElementById('client_name_info').innerText = client_name
        document.getElementById('lotName_info').innerText = lote
        document.getElementById('work_order_info').innerText = wo
        document.getElementById('filter_info').innerText = filter
        document.getElementById('formula_info').innerText = color_formula
        document.getElementById('model_info').innerText = model
        document.getElementById('container_info').innerText = pieces
        /* document.getElementById('base_info').innerText = baseWeight */
        $('#infoProcessModal').modal('show')
        console.log(list_MixProcess)
    } else {
        $('#errorInfoModal').modal('show')
    }

})

$('#errorInfoModal').on('shown.bs.modal', () => {
    setTimeout(() => {
        $('#errorInfoModal').modal('hide')
    },5000)
})

async function startFill(){
    const date = new Date()
    /* list_MixProcess.num_containers = parseInt(containers) */    
    initial_info.order_work = wo
    list_MixProcess.number_of_pieces = parseInt(pieces)
    list_MixProcess.t_start = date.toISOString()
    console.log(list_MixProcess)
    await post_process(list_MixProcess)
    var response_api = api_response
    if(response_api.data.rest == "SUCCESS") {
        localStorage.setItem('base_weigth', list_MixProcess.conatiner_base_weight)
        localStorage.setItem('num_containers', parseInt(response_api.data.num_containers))
        localStorage.setItem('id_process', parseInt(response_api.data.id))
        localStorage.setItem('initial_info', JSON.stringify(initial_info))
        localStorage.setItem('mixProcess', JSON.stringify(list_MixProcess))
        localStorage.setItem('last_container_weight', response_api.data.last_container_base_weight)
        window.location.replace("/mixing/containers")
    }
}

function editInfo() {
    window.location.reload()
}

function backPage() {
    window.location.replace('/')
}

function continuePage() {
    window.location.replace('/mixing/containers/')
}

function fullPage(){
    console.log("Entra")
    page.requestFullscreen()
}