var ele = sessionStorage.getItem('containers')
var bases = []

for (let index = 0; index < ele; index++) {
    document.getElementById('content').innerHTML += `
        <div class="mb-4" style="width:725px">
            <input class="form-check-input" type="checkbox" name="radioButton" id="radioBtn1" value="${index + 1}" disabled>
            <b> Contenedor #${index+1} </b>
            <button style="float: right;" type="button" class="btn btn-success"  data-item-id="0" id="fill_start" value="${index}" onclick="startComponent()">Iniciar Llenado</button>   
        </div>
    `
}

$(document).ready(() => { 
    var ele = document.querySelectorAll('input[type=checkbox]')
    var btn = ele[0]
    if(localStorage.getItem("chkId")){
        btn.checked = "true"
    }
})
function startComponent(){
    var id = sessionStorage.getItem('id')
    window.location.href = `http://127.0.0.1:5000/mixing/containers/component/${id}`
}