let chars_temperature = []
let chars_humidity = []
let chars_viscosity = []

let chars_wo =[]
let chars_container = []

const btn_ok = document.getElementById('btn-temperature')


function keyBoardInformationContainer(element){
    document.getElementById('button-humidity').disabled = true
    document.getElementById('button-viscosity').disabled = true
    btn_ok.disabled = true
    if(element.value == "0"){
        document.getElementById('temperature').style.border = "5px solid blue";
        document.getElementById('button-humidity').disabled = true
        document.getElementById('button-viscosity').disabled = true
        console.log('Entra Temperatura')
        document.getElementById('keyboard-temp').style.display = 'flex'
        var input_area_temp = document.getElementById('temperature_id_0')
        var btns_temperature = document.querySelectorAll('.btn-key-temp')
        var btn_delete_temp = document.querySelector('.delete-temp')
        var btn_enter_temp = document.querySelector('.enter-temp')
        btns_temperature.forEach(btn_t => {
            btn_t.addEventListener('click', () => {
                input_area_temp.value += btn_t.innerText
                chars_temperature = input_area_temp.value.split('')
            })
        })

        btn_delete_temp.addEventListener('click', () => {
            chars_temperature.pop()
            input_area_temp.value = chars_temperature.join('')
        })

        btn_enter_temp.addEventListener('click', () => {
            if(input_area_temp.value == "" ){
                document.getElementById('field').innerText = improved_mix.subtitle_modal_tem
                $('#errorEmptyModal').modal('show')                
            } else {
                parseInt(input_area_temp.value)
                if(input_area_temp.value >= 0 && input_area_temp.value <= 100){
                    document.getElementById('value-input-temp').innerText =  `${input_area_temp.value} °C`
                    $('#ensureInfoModal').modal('show')
                } else {
                    $('#errorExcessTempModal').modal('show')
                }
            }
        })
    } else if(element.value == "1") {
        document.getElementById('humidity').style.border = "5px solid blue";
        document.getElementById('button-temperature').disabled = true
        document.getElementById('button-viscosity').disabled = true
        console.log('Entra Humedad')
        document.getElementById('keyboard-humidity').style.display = 'flex'
        var input_area_humidity = document.getElementById('humidity_id_1')
        var btns_humidity = document.querySelectorAll('.btn-key-humidity')
        var btn_delete_humidity = document.querySelector('.delete-humidity')
        var btn_enter_humidity = document.querySelector('.enter-humidity')
        btns_humidity.forEach(btn_h => {
            btn_h.addEventListener('click', () => {
                input_area_humidity.value += btn_h.innerText
                chars_humidity = input_area_humidity.value.split('')
            })
        })

        btn_delete_humidity.addEventListener('click', () => {
            chars_humidity.pop()
            input_area_humidity.value = chars_humidity.join('')
        })
        
        btn_enter_humidity.addEventListener('click', () => {
            if(input_area_humidity.value == "" ){
                document.getElementById('field').innerText = improved_mix.subtitle_modal_hum
                $('#errorEmptyModal').modal('show')                
            } else {
                parseFloat(input_area_humidity.value)
                if(input_area_humidity.value >= 0 && input_area_humidity.value <= 100){
                    document.getElementById('value-input-hum').innerText =  `${input_area_humidity.value} %`
                    $('#ensureHumModal').modal('show')
                } else {
                    $('#errorExcessHumModal').modal('show')
                }
            }
        })
    } else if(element.value == "2") {
        document.getElementById('viscosity').style.border = "5px solid blue";
        document.getElementById('button-temperature').disabled = true
        document.getElementById('button-humidity').disabled = true
        console.log('Entra Viscosidad')
        document.getElementById('keyboard-viscosity').style.display = 'flex'
        var input_area_viscosity = document.getElementById('viscosity_id_2')
        var btns_viscosity = document.querySelectorAll('.btn-key-viscosity')
        var btn_delete_viscosity = document.querySelector('.delete-viscosity')
        var btn_enter_viscosity = document.querySelector('.enter-viscosity')
        btns_viscosity.forEach(btn_v => {
            btn_v.addEventListener('click', () => {
                input_area_viscosity.value += btn_v.innerText
                chars_viscosity = input_area_viscosity.value.split('')
            })
        })

        btn_delete_viscosity.addEventListener('click', () => {
            chars_viscosity.pop()
            input_area_viscosity.value = chars_viscosity.join('')
        })

        btn_enter_viscosity.addEventListener('click', () => {
            if(input_area_viscosity.value == "" ){
                document.getElementById('field').innerText = improved_mix.subtitle_modal_vis
                $('#errorEmptyModal').modal('show')                
            } else {
                parseInt(input_area_viscosity.value)
                if(input_area_viscosity.value > 0){                    
                    document.getElementById('value-input-visco').innerText =  `${input_area_viscosity.value} s`
                    $('#viscoInfoModal').modal('show')
                } else {
                    $('#errorExcessViscoModal').modal('show')
                }
            }
        })
    }
}

$('#errorEmptyModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorEmptyModal').modal('hide')
    },7000)
})

$('#errorExcessHumModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorExcessHumModal').modal('hide')
    },7000)
})

$('#errorExcessTempModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorExcessTempModal').modal('hide')
    },7000)
})

$('#errorExcessViscoModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorExcessViscoModal').modal('hide')
    },7000)
})

$('#add-WorkOrder').click(function(){
    document.getElementById('insertDataModalLabel').textContent = `${wo_detail_language.process_title_wo}`
    document.getElementById('keyboard-wo').style.display = 'flex'
    var btns_wo = document.querySelectorAll('.btn-key-wo')
    var input_area_wo = document.getElementById('information-wo')    
    document.getElementById('information-container').style.display = 'none'
    const btn_delete_wo = document.querySelector('.delete-wo')
    const btn_enter_wo = document.querySelector('.enter-wo') 
    
    btns_wo.forEach(btn => {
        btn.addEventListener('click', () => {
            console.log()
            input_area_wo.value += btn.innerText
            chars_wo = input_area_wo.value.split('')
        })
    })

    btn_delete_wo.addEventListener('click', () => {
        chars_wo.pop()
        input_area_wo.value = chars_wo.join('')
    })

    btn_enter_wo.addEventListener('click', () => {
        var value_wo = document.getElementById('information-wo').value
        if(value_wo == ''){
            $('#errorKeyBoardModal').modal('show')
        } else if(value_wo.length == 10){
            $('#ensureWOModal').modal('show')
        } else {
            $('#errorLenghtModal').modal('show')
        }
    })   
})

$('#errorKeyBoardModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorKeyBoardModal').modal('hide')
    }, 6000)
})

$('#errorLenghtModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorLenghtModal').modal('hide')
    }, 6000)
})

$('#ensureWOModal').on('show.bs.modal', () => {
    var input_area_wo = document.getElementById('information-wo')
    document.getElementById('value-input-wo').innerText = input_area_wo.value
})

function addWorkOrder(){
    var input_keyboard = document.getElementById('information-wo').value
    document.getElementById('input-area-0').value =  input_keyboard
    document.getElementById('information-container').style.display = ''
    document.getElementById('information-wo').style.display = ''
    document.getElementById('add-WorkOrder').disabled = true
    document.getElementById('keyboard-wo').style.display = 'none'
    $('#ensureWOModal').modal('hide')
    $('#insertDataModal').modal('hide')
}


$("#add-Pieces").click(function(){
    var value_btn = $(this).val()
    document.getElementById('insertDataModalLabel').textContent = `${wo_detail_language.process_title_pz}`
    document.getElementById('keyboard-container').style.display = 'flex'
    document.getElementById('information-wo').style.display = 'none'
    var input_area_container = document.getElementById('information-container')
    var btns_container = document.querySelectorAll('.btn-key-container')
    const btn_delete_container = document.querySelector('.delete-container')
    const btn_enter_container = document.querySelector('.enter-container') 
    
    btns_container.forEach(btn => {
        btn.addEventListener('click', () => {
            input_area_container.value += btn.innerText
            chars_container = input_area_container.value.split('')
            console.log(chars_container)
        })
    })
    
    btn_delete_container.addEventListener('click', () => {
        chars_container.pop()
        input_area_container.value = chars_container.join('')
    })

    btn_enter_container.addEventListener('click', () => {
        var value_container = document.getElementById('information-container').value
        if(value_container == ''){
            $('#errorKeyBoardModal').modal('show')
        } else if(value_container != '0'){
            $('#ensureContainerModal').modal('show')
        } else {
            $('#errorCeroModal').modal('show')
        }
    })
})

$('#ensureContainerModal').on('show.bs.modal', () => {
    var input_area_container = document.getElementById('information-container')
    console.log(input_area_container.value)
    document.getElementById('value-input-conatiner').innerText = `${input_area_container.value}`
})

$('#errorCeroModal').on('show.bs.modal', () => {
    setTimeout(() => {
        $('#errorCeroModal').modal('hide')
    }, 6000)
})

function addContainer(){
    var input_area_container = document.getElementById('information-container')
    console.log(input_area_container.value)
    document.getElementById('value-input-conatiner').innerText = input_area_container.value
    
    document.getElementById('keyboard-container').style.display = 'none'
    document.getElementById('input-area-1').value = input_area_container.value
    document.getElementById('information-container').style.display = ''
    document.getElementById('information-wo').style.display = ''
    document.getElementById('add-Pieces').disabled = true
    $('#ensureContainerModal').modal('hide')
    $('#insertDataModal').modal('hide')
}

$('#errorExcessTempModal').on('show.bs.moda', () => {
    setTimeout(() => {
        $('#errorExcessTempModal').modal('hide')
    }, 6000)
})

function addTempCategory(){
    btn_ok.disabled = false
    document.getElementById('button-temperature').disabled = true
    document.getElementById('button-humidity').disabled = false
    document.getElementById('temperature').style.border = "";
    $('#ensureInfoModal').modal('hide')
    document.getElementById('keyboard-temp').style.display = 'none'
}

function addHumCategory(){
    btn_ok.disabled = false
    document.getElementById('button-humidity').disabled = true
    document.getElementById('button-viscosity').disabled = false
    document.getElementById('keyboard-humidity').style.display = 'none'
    document.getElementById('humidity').style.border = "";
    $('#ensureHumModal').modal('hide')
}

function addViscoCategory(){
    btn_ok.disabled = false
    document.getElementById('button-humidity').disabled = true
    document.getElementById('button-viscosity').disabled = true
    document.getElementById('keyboard-viscosity').style.display = 'none'
    document.getElementById('viscosity').style.border = "";
    $('#viscoInfoModal').modal('hide')
}