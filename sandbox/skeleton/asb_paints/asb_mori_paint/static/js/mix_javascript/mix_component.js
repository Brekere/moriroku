/* var radio_btn = undefined
var btns = [] */


var index_btn = 0
var btn = undefined
var weight_Subs = 0
var expected_weight = 0
var weight_base = 8000
var weight_container_limit = 12000
var percent_Subs = 0
var index_title = 1
var index_weight = 0
document.getElementById(`container-count`).textContent = `Contenedor ${index_title}/${list_json.length}`

btn = btns[index_btn]

var btn_readyG = document.getElementById('readyGraphBtn')
var btn_readyG2 = document.getElementById('readyGraphBtn2')
var btn_readyG3 = document.getElementById('readyGraphBtn3')

function example(element){
    expected_weight = 8000 * total_percent
    for (let index_js = 0; index_js < list_json.length; index_js++) {
        if(list_json[index_js]['name_component'] === element.value){            
            var weight = (list_json[index_js]['percent']/100) * 8000
            weight_Subs += weight
            document.getElementById(`weight-${index_js}`).textContent = `${weight} g`
            document.getElementById(`container-count`).textContent = `Contenedor ${index_js+1}/5`
            document.getElementById(`weigth-total`).textContent = `${weight_Subs} g`
            document.getElementById('percent').textContent = `${((weight_Subs/expected_weight)*100).toFixed(2)} %`
            index_js = index_js + 1
        }
    }

    btn.style.display = 'none'
    radio_btn[index_btn].checked = true
    index_btn++
    btn = btns[index_btn]
    btn.style.display = 'inline'
}

function update_levels_loop(){
    var ele = document.getElementById('fillLeves-container')
    get_weight(port_loop);
    draw_fill_levels_stacked_bar(ele.id);
}

function eclick(element){
    document.getElementById('substance').textContent = element.value
    expected_weight = 8000 * total_percent
    var tolerance = 0    
    var last_subs = list_json[list_json.length-1]['name_component']
    for (let index_js = 0; index_js < list_json.length; index_js++) {
        if(list_json[index_js]['name_component'] === element.value){
            tolerance = list_json[index_js]['tolerance']
            percent_Subs = list_json[index_js]['percent']
            index_js = list_json.length
        }
    }
    init_values(weight_base, weight_container_limit, tolerance)

    if(btn.value != last_subs){
        $('#containerModal').modal('show')
        btn_readyG2.style.display = 'none'
        btn_readyG3.style.display = 'none'
    } else {
        $('#codeReadModal').modal('show')
        btn_readyG2.style.display = 'inline'
        btn_readyG3.style.display = 'none'
    }
}


function readyBtn(){
    $('#containerModal').modal('hide')
    $('#calibrationModal').modal('show')
}

$('#calibrationModal').on('shown.bs.modal', function() {
    const timer = 4000
    setTimeout(function(){
        $('#calibrationModal').modal('hide')
        $('#sustModal').modal('show')
    },timer)
})

/* function example(){
    console.log("este",refreshIntervalId_update_weight)
    var weight = gr_level
    debugger
    clearInterval(refreshIntervalId_update_weight);
    $('#sustModal').modal('hide')
    $('#sustMixModal').modal('show')    
    console.log("este",refreshIntervalId_update_weight)
} */

btn_readyG.addEventListener('click', () => {
    const timer = 4000

    if(level < 90){
        document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Abajo'
        document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de bajo del promedio. Favor de vertir más sustancia.'
        $('#graphWarnModal').modal('show')
        $('#graphWarnModal').on('shown.bs.modal', () => {
            setInterval(function(){
                $('#graphWarnModal').modal('hide')
            }, timer)
        })
    } else {
        if(level >= 105 && level <= 120){
            document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Encima'
            document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de encima del promedio. Favor de quitar sustancia.'
            $('#graphWarnModal').modal('show')
            $('#graphWarnModal').on('shown.bs.modal', () => {
                setInterval(function(){
                    $('#graphWarnModal').modal('hide')
                }, timer)
            })
        } else {
            if(level > 90 && level < 105){
                clearInterval(refreshIntervalId_update_weight);
                loop_w = false;
                port_loop = "";
                refreshIntervalId_update_weight = null;
                console.log("Ciclo terminado!!!");
                $('#sustModal').modal('hide')
                $('#successModal').modal('show')
                
            }
        }
    }
})  

$('#successModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#successModal').modal('hide')
    }, 3500)

    paintWeight(1)

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
            document.getElementById(`weight-${index_weight}`).textContent = `${weight} g`
            document.getElementById(`container-count`).textContent = `Contenedor ${index_title+1}/${list_json.length}`
            document.getElementById(`weigth-total`).textContent = `${weight_Subs} g`
            document.getElementById('percent').textContent = `${((weight_Subs/expected_weight)*100).toFixed(2)} %`
            index_weight = index_weight + 1
            break;
            case 2:
                var weight = gr_level
                weight_Subs += weight
                document.getElementById(`weight-${index_weight}`).textContent = `${weight} g`
                document.getElementById(`weigth-total`).textContent = `${weight_Subs} g`
                document.getElementById('percent').textContent = `${((weight_Subs/expected_weight)*100).toFixed(2)} %`
                break;
            }
}


/* PROCESO DE LLENADO DEL CONTENEDOR */ 

$('#codeReadModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#codeReadModal').modal('hide')        
        $('#paintContainerModal').modal('show')        
    }, 3000)
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



function readyMix(btn_value){
    const timer = 4000

    if(level < 90){
        document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Abajo'
        document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de bajo del promedio. Favor de vertir más sustancia.'
        $('#graphWarnModal').modal('show')
        $('#graphWarnModal').on('show.bs.modal', () => {
            setInterval(function(){
                $('#graphWarnModal').modal('hide')
            }, timer)
        })
    } else {
        if(level >= 105 && level <= 120){
            document.getElementById('graphWarnModalLabel').textContent = 'Alerta: Nivel Por Encima'
            document.getElementById('errorBody').textContent = 'La sustancia vertida esta por de encima del promedio. Favor de quitar sustancia.'
            $('#graphWarnModal').modal('show')
            $('#graphWarnModal').on('show.bs.modal', () => {
                setInterval(function(){
                    $('#graphWarnModal').modal('hide')
                }, timer)
            })
        } else {
            if(level > 90 && level < 105){
                switch(btn_value){
                    case 1:
                        $('#successPaintModal').modal('show')
                        $('#successPaintModal').on('shown.bs.modal', () => {
                            setInterval(function(){
                                init_values(expected_weight, weight_container_limit, .05)
                                btn_readyG2.style.display = 'none'
                                btn_readyG3.style.display = 'inline'
                                $('#successPaintModal').modal('hide')
                            }, timer)
                        })
                        paintWeight(2)
                        btn.style.display = 'none'
                        radio_btn[index_btn].checked = true
                        break;
                    case 2:
                        clearInterval(refreshIntervalId_update_weight);
                        refreshIntervalId_update_weight = null;
                        console.log("Ciclo terminado!!!");
                        $('#sustMixModal').modal('hide')
                        $('#timerModal').modal('show')                        
                        break
                }                                
            }
        }
    }
}

$('#timerModal').on('shown.bs.modal', function(){
    var sec = 30
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

 function addTemperature(){
    $('#timerModal').modal('hide')
    $('#temperatureModal').modal('show')
}

function viscosityCheck(){
   //const viscosity = (Math.random(1) * 15).toFixed(0)
   const viscosity = 23;
   var value = document.getElementById('visco').value
   if(value != viscosity){
       $('#viscosityModal').modal('hide')
       $('#adjustviscoModal').modal('show')
   } else {
       $('#viscosityModal').modal('hide')
       generateQR()
       $('#reportModal').modal('show')
    }
}

function generateQR(){ 
    const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 
    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

   var d = new Date()
   var date = d.getDate() + '/' + months[d.getMonth()] + '/' + d.getFullYear()
   var time = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds()
   var datetime = date + " " + time

   var qrcode = undefined
   if(qrcode === undefined){
       qrcode = new QRCode(document.getElementById('qr'), {
           text: `Number OT: ${document.getElementById('OT').textContent} \n
                  Date: ${datetime} \n
                  Startime/Endtime: 16:18 - 16:55 \n
                  Opeartor Name: ${document.getElementById('OPName').textContent}
                  Batch Number: 8967602 \n
                  Rework Info: RS \n
                  Filter Information: 98HGN.2mm`,
       }) 
       qrcode = new QRCode(document.getElementById('qr'), {
           text: `Number OT: ${document.getElementById('OT').textContent} \n
                  Date: ${datetime} \n
                  Startime/Endtime: 16:18 - 16:55 \n
                  Opeartor Name: ${document.getElementById('OPName').textContent}
                  Batch Number: 8967602 \n
                  Rework Info: RS \n
                  Filter Information: 98HGN.2mm`,
       }) 
   } else {
       qrcode.clear()
       qrcode.makeCode(document.getElementById('qr'), {
           text: `Number OT: ${document.getElementById('OT').textContent} \n
                  Date: ${datetime} \n
                  Startime/Endtime: 16:18 - 16:55 \n
                  Opeartor Name: ${document.getElementById('OPName').textContent}
                  Batch Number: 8967602 \n
                  Rework Info: RS \n
                  Filter Information: 98HGN.2mm`,
       })
   }
}

function temperatureAdded(){
   var temp = document.getElementById('temperature_id').value
   var hum = document.getElementById('humidity_id').value
   if(temp != '' && hum != ''){
       $('#temperatureModal').modal('hide')
       $('#viscosityModal').modal('show')
   }
}

$('#adjustviscoModal').on('shown.bs.modal', function() {
   const timer = 7000
   setInterval(function(){
       $('#adjustviscoModal').modal('hide')
       window.location.replace('http://127.0.0.1:5000/improvedMix')
   }, timer)
})