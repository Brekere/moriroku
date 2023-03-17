var list_MixProcess = JSON.parse(localStorage.getItem('mixProcess'))
var containers = localStorage.getItem('num_containers')
var id_process = parseInt(localStorage.getItem('id_process'))
let last_base_weight = parseInt(localStorage.getItem('last_container_weight'))
let result_fullpage = localStorage.getItem('full_screen')
let btn_back = document.getElementById('back')

console.log(result_fullpage)
console.log(typeof(result_fullpage))
var btn_start_fill = undefined

console.log(list_MixProcess)

var bases = []
const date = new Date()

list_Container = {
    "id_barcode" : "",
    "id_process" : "",
    "viscosity" : "",
    "weight" : "",
    "humidity" : "",
    "temperature" : "",
    "t_start" : "",
    "t_end" : "",
    "t_start_tare" : "",
    "t_end_tare" : "",
    "t_start_container" : "",
    "t_end_container" : "",
    "t_start_viscosity" : "",
    "t_end_viscosity" : "",
    "rework" : ""
}

list_start = {
    "id_process" : id_process,
    "t_start" : ""
}

mix_proces_end = {
    "id" : id_process,
    "t_end" : "",
}

let struct_error_process = {
    "id" : id_process,
    "failed_process": "",
    "failure_type": "",
    "failure_description": ""
}

console.log(id_process)

$(document).ready(() => { 
    var index_check = parseInt(localStorage.getItem('chkId'))
    console.log(index_check)
    btn_start_fill = document.querySelectorAll('#fill_start')
    var ele = document.querySelectorAll('input[type=checkbox]')    
    if(index_check != 0){
        for (let index = 0; index <= index_check; index++) {
            listContainer = JSON.parse(localStorage.getItem(`mixContainer-${index}`))
            document.getElementById(`total-weight-${index}`).innerText = `${(listContainer.weight).toFixed(0)} g`
            var btn_fill = btn_start_fill[index]
            var btn = ele[index]
            btn.checked = true
            btn_fill.style.display = 'none'
            btn_back.style.display = 'none'
            if(index != btn_start_fill.length-1){
                var btn_fill = btn_start_fill[index+1]
                btn_fill.removeAttribute("disabled")
            }
        }
        for (let index = 0; index < ele.length; index++) {
            if(ele[ele.length-1].checked){
                btn_back.style.display = 'none'
                document.getElementById('end-process').style.display = 'inline'
            }
        }        
    } else {
        var listContainer = JSON.parse(localStorage.getItem(`mixContainer-${index_check}`))
        document.getElementById(`total-weight-${index_check}`).innerText = `${(listContainer.weight).toFixed(0)} g`
        var btn_fill = btn_start_fill[index_check]
        var btn = ele[index_check]
        btn.checked = "true"
        btn_fill.style.display = 'none'
        btn_back.style.display = 'none'
        if(containers != 1){
            index_check++
            btn_fill = btn_start_fill[index_check]
            btn_fill.removeAttribute("disabled")                
        } else {
            list_MixProcess.g = document.getElementById('total-weight-0').textContent
            document.getElementById('end-process').style.display = 'inline'
        }
    }
    localStorage.setItem('chkId', index_check)
})

for (let index = 0; index < containers; index++) {
    if(index == 0)
        document.getElementById('content').innerHTML += `
            <div class="mb-3">
                <input class="form-check-input" type="checkbox" name="radioButton" id="radioBtn1" value="${index + 1}" disabled>
                <b id="container"> Contenedor #</b><b>${index+1}</b>
                <span>
                    <b id="total-weight-${index}"> </b>
                    <button type="button" class="btn btn-success" data-item-id="0" id="fill_start" value="${index}" onclick="startComponent(this.value)">Iniciar Llenado</button>   
                </span>
            </div>
        `
    else{
        document.getElementById('content').innerHTML += `
            <div class="mb-3">
                <input class="form-check-input" type="checkbox" name="radioButton" id="radioBtn1" value="${index + 1}" disabled>
                <b id="container"> Contenedor #</b>${index+1}
                <span>   
                    <b id="total-weight-${index}"> </b>
                    <button  type="button" class="btn btn-success" data-item-id="0" id="fill_start" value="${index}" onclick="startComponent(this.value)" disabled>Iniciar Llenado</button>   
                </span>
            </div>
        `
    }
}


async function sendData(){
    const date = new Date()
    
    mix_proces_end["t_end"] = date.toISOString()
    await post_process(mix_proces_end)
    console.log(api_response)
    localStorage.clear()
    window.location.href = '/'
}


async function startComponent(value){
    const date = new Date()
    list_start['t_start'] = date.toISOString()
    console.log(list_start)
    await post_container(list_start)
    var id_component = api_response.data.id // cambiar nombre de id_componnet  a id_conteiner
    localStorage.setItem('id_component', id_component)
    localStorage.setItem('actual_container', parseInt(value)+1)
    var btn_start_fill = document.querySelectorAll('#fill_start')
    console.log(btn_start_fill[btn_start_fill.length-1].value)
    console.log("Value", value)
    if(value == btn_start_fill[btn_start_fill.length-1].value){
        var base_w = localStorage.getItem('base_weigth')
        var base_last_w = localStorage.getItem('last_container_weight')
        base_w = base_last_w
        localStorage.setItem('base_weigth', base_w)
    }
    localStorage.setItem(`mixContainer-${value}`, JSON.stringify(list_Container))
    var len_btns = btn_start_fill.length
    var id = list_MixProcess.id_formula
    var list_Container_index = JSON.parse(localStorage.getItem(`mixContainer-${value}`))
    list_Container_index.t_start = date.toISOString()
    localStorage.setItem(`mixContainer-${value}`, JSON.stringify(list_Container_index))
    localStorage.getItem(`mixContainer-${value}`)
    localStorage.setItem('chkId', parseInt(value))
    localStorage.setItem('lenBtns', parseInt(len_btns))
    window.location.href = `/mixing/containers/component/${id}`
}

function backPage() {
    window.location.replace('/OT_Detail')
}

async function pruebaError(){
    struct_error_process["failed_process"] = true
    struct_error_process["failure_type"] = 0
    struct_error_process["failure_description"] = "La temperatura esta fuera del limite establecido."
    console.log(struct_error_process)
    await post_process_errors(struct_error_process);
    console.log(api_response)
}