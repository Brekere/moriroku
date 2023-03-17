document.getElementById('fill_pro').focus()
let btn_fullscreen = document.querySelector('#maximize')
let btn_minimize = document.querySelector('#minimize')
let full_page = false

var listW = []

//departaments_json = JSON.parse(elements)
CredentialsZPLModal
struct_departament = {
  "departament": "",
  "password": ""
}

let struct_error_info = {
  
}

localStorage.clear()

/* list_MixProcess = {
  "id_worker" : "",
  "name_worker": "",
  "id_formula" : "",
  "id_filter": "",
  "conatiner_base_weight": ,
  "t_start" : "",
  "expected_viscosity_min" : "",
  "expected_viscosity_max" : "",
  "number_of_pieces" : "",
  "grams_to_recirculate" : 3000,
  "work_order": "",
  "id_model": ""
} */

list_MixProcess = {
  "id_worker" : 1,
  "name_worker": "Franco Maldonado Fuerte",
  "id_formula" : 1,
  "id_filter" : 2,
  "conatiner_base_weight": 12000,
  "t_start" : "2022-06-28T22:34:38.598Z",
  "expected_viscosity_min" : 236,
  "expected_viscosity_max" : 242,
  "number_of_pieces" : "",
  "grams_to_recirculate" : 3000,
  "work_order": "",
  "id_model": ""
}

function loadJSFile(){
  var scriptTag = document.createElement("script");
  scriptTag.setAttribute("type", "text/javascript");
  scriptTag.setAttribute("src", "static/js/scanner_connection/scanner.js");
  
  var head = document.getElementsByTagName("head")[0];
  head.appendChild(scriptTag);
}

$('#infoModal').on('shown.bs.modal', function () {
  const time = 5000
  setTimeout(function(){
    $('#infoModal').modal('hide')
    r = 4
    loadJSFile()
    $('#CredentialsModal').modal('show')
  }, time)
});

$('#CredentialsModal').on('show.bs.modal', async () => {
  const timer = 7000
  await get_nextid_proces()
  setTimeout(() => {
    $('#CredentialsModal').modal('hide')
    window.localStorage.setItem('full_screen', full_page)
    window.localStorage.setItem('mixProcess', JSON.stringify(list_MixProcess))
    var next_id_proces = response_data
    window.localStorage.setItem('next_id', next_id_proces.next_id)
    window.location.href = '/OT_Detail'
  }, timer)
})

$('#CredentialsZPLModal').on('show.bs.modal', () => {
  loadJSFile()
  r = 10
})

async function testRegister(){
  let password = document.getElementById('pass').value
  let departament = document.getElementById('departamento').value
  if(password != "" && departament != ""){
    struct_departament['departament'] = departament
    struct_departament['password'] = password
    await post_register_departament(struct_departament)
    var response = api_response
    console.log(response.data.rest)
    if(response.data.rest == "SUCCESS") {
      alert("Registro Completado")
    } else {
      alert("No se ha podido registrar")
    }
  } else {
    alert("Campos Vacios")
  }
}

async function example(){
  await get_zpl_info_by_id(6)
  var response = identifie_response
  console.log(response)
}

async function testValidation(){
  let date = new Date();
  zpl = {
    'id' : 5,
    'zpl_code' : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'creation_date' : date.toISOString(),
    "update_date": date.toISOString()
  }
  await post_test_zpl(zpl)
}

function sum(hum, temp){
  const min_temp = 20.0
  const max_temp = 24.0
  const min_hum = 30.0
  const max_hum = 70.0  
  if(temp >= min_temp && temp <= max_temp && hum >= min_hum && hum <= max_hum){
    return null
} else if(temp < min_temp){
  if(hum < min_hum || hum > max_hum){
    return 'both'
  } else {
    return 'temperature'
  }
} else if(temp > max_temp) {
  if(hum < min_hum || hum > max_hum){
    return "both"
  } else {
    return 'temperature'
  }
} else if(hum > max_hum) {
  if(temp < min_temp && temp > max_temp){
    return "both"
  } else {
    return 'humidity'
  }
} else if(thum < min_hum) {
  if(temp < min_temp && temp > max_temp){
    return "both"
  } else {
    return 'humidity'
  }
}

} 

function openserverurl(url){
  window.location.href=url
}