var index = '1'
var containers = 0
var WO = ''
var id_formula = 0

var error_index = -1

var colors = []
var model = []
var filter = []

document.getElementById('lotName').innerText = (index + '').padStart(7, '0')

const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

var d = new Date()
var date = d.getDate() + '/' + months[d.getMonth()] + '/' + d.getFullYear()
var time = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds()
var datetime = date + " " + time

document.getElementById('datetime').innerHTML = datetime

function filterSelect(value, list){
    if(value.value != -1){
        var decode_Json = JSON.parse(list)
        var name_filter = decode_Json.find(x => x.id_formula == value.value)
        name_filter = name_filter['name_filtro']
        var data = document.getElementById('select-form-color')
        document.getElementById('filterSelected').style.display = 'inline'
        id_formula = data.options[data.selectedIndex].value
        error_index = id_formula
        document.getElementById('filter').textContent = name_filter
    } else {
        error_index = -1
        document.getElementById('filter').textContent = ''
        document.getElementById('filterSelected').style.display = 'none'
    }
}

function example(value, list){
    var decode_Json = JSON.parse(list)
    var name_filter = decode_Json.find(x => x.id_formula == value.value)
    name_filter = name_filter['name_filtro']
    console.log(name_filter)
}

function startFill(){
    WO = document.getElementById('WO').value
    containers = document.getElementById('containersQ').value
    if(WO != '' && containers != '' && error_index != -1){
        sessionStorage.clear()
        console.log(id_formula)
        sessionStorage.setItem('id', id_formula)
        sessionStorage.setItem('containers', parseInt(containers))
        window.location.href = "http://127.0.0.1:5000/mixing/containers"
    }else{
        console.log("Error")
    }
}

/* function startFill(){
    localStorage.clear()
    var data = document.getElementById('select-form-color')
    var form = data.options[data.selectedIndex].text
    containers = parseInt(document.getElementById('containersQ').value)
    sessionStorage.setItem('container', containers)
    sessionStorage.setItem('form', form)
    window.location.href = "http://127.0.0.1:5000/mixing/containers"
} */