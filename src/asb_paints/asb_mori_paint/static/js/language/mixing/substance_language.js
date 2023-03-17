let language_json = undefined
let substance_language = undefined
let container_label_var = undefined

let text_title = document.getElementById('title')
let text_lang_drop = document.getElementById('lang_drop')
let text_spanish = document.getElementById('spanish')
let text_english = document.getElementById('english')

let weight_total_label = document.getElementById('weight-title')
let barcode_label = document.getElementById('barcode')
let jug_label = document.querySelectorAll('#jug_name')
let container_label = document.getElementById('container_name')

let modal_WorkValidationTL_title = document.getElementById('workerValidationModalLabel')
let modal_WorkValidationTL_body = document.getElementById('workerValidation-body')
let modal_WorkValidationTL_1_title = document.getElementById('workerValidationTLModalLabel')
let modal_WorkValidationTL_2_body = document.getElementById('workerValidationTL-body')
let modal_ScanComponent_title = document.getElementById('componentCheckModalLabel')
//let modal_WorkValidationTL_2_body = document.getElementById('workerValidationTL-body')

let btn_start_fill_label = document.querySelectorAll('#fill_start')

let session_strg_list_lang = JSON.parse(sessionStorage.getItem('list_language'))
let session_strg_lang = sessionStorage.getItem('language')

fetch('/static/config_json/language.json').then(response => {
    return response = response.json()
}).then( data => {
    language_json = data
})

if(session_strg_lang == 'eng'){
    changeLanguagePage(session_strg_list_lang)
} else if (session_strg_lang == 'esp'){
    substance_language = session_strg_list_lang.Component_list
}

function languageSelect(lan){
    list_lang = language_json[0]['list']
    console.log(list_lang)
    console.log(lan)
    lan == 'esp' ? language = 'Spanish' : language = 'English'
    console.log(language)
    for (let index = 0; index < list_lang.length; index++) {
        if(list_lang[index]['language'] == language){
            list_lang = list_lang[index]['esp']        
        } else {
            list_lang = list_lang[index+1]['eng']
        }
    }
    
    
    sessionStorage.setItem('list_language', JSON.stringify(list_lang))
    sessionStorage.setItem('language', lan)
    changeLanguagePage(list_lang)
}

function changeLanguagePage(list_lang_){
    text_title.textContent = list_lang_.title_nav
    text_lang_drop.textContent = list_lang_.languages
    text_spanish.textContent = list_lang_.spanish
    text_english.textContent = list_lang_.english
    substance_language = list_lang_.Component_list
    weight_total_label.textContent = substance_language.tot_weight
    document.getElementById(`container-count`).textContent = `${substance_language.title_container} ${index_title}/${list_json.length}`
    barcode_label.textContent = substance_language.barcode_label
    for (let index = 0; index < btn_start_fill_label.length; index++) {
        btn_start_fill_label[index].textContent = substance_language.btn_start_fill
    }

    for (let index = 0; index < jug_label.length; index++) {
        jug_label[index].textContent = substance_language.jug        
    }
    container_label.textContent = substance_language.container

    modal_WorkValidationTL_title.textContent = substance_language.scan_worker_modal
    modal_WorkValidationTL_body.textContent = substance_language.scan_worker_modal_body
    modal_WorkValidationTL_1_title.textContent = substance_language.scan_worker_modal
    modal_WorkValidationTL_2_body.textContent = substance_language.scan_worker_modal_body

    modal_ScanComponent_title.textContent = substance_language.scan_component_title
}