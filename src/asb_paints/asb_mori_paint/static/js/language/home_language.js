let language_json = undefined
let language = undefined
let list_lang = undefined
let text_title = document.getElementById('title')
let text_lang_drop = document.getElementById('lang_drop')
let text_spanish = document.getElementById('spanish')
let text_english = document.getElementById('english')
let text_zpl_btn = document.getElementById('zpl')
let text_fill_btn = document.getElementById('fill_pro')
let text_visco_btn = document.getElementById('viscosity_pro')
let text_modal_info_title = document.getElementById('infoModalLabel')
let text_modal_info_body_cred = document.getElementById('body-info-cred')
let text_modal_proc_body_cred = document.getElementById('body-process-cred')
let text_modal_proc_body_print = document.getElementById('reprintBodyModal')
let text_modal_error_title = document.getElementById('errorModalLabel')
let text_modal_error_p1 = document.getElementById('body-p1')
let text_modal_error_p2 = document.getElementById('body-p2')

let mix_modal_info = document.getElementById('infoMixModalLabel')
let color_label_modal = document.getElementById('color_label')
let viscosity_label_modal = document.getElementById('viscosity_label')
let improvement_btn_start = document.getElementById('improvementS')
let improvement_btn_close = document.getElementById('improvementClose')

let scan_worker_modal = document.getElementById('worker-scan-body')
let scan_container_modal = document.getElementById('container-scan-body')

let session_strg_list_lang = JSON.parse(sessionStorage.getItem('list_language'))
let session_strg_lang = sessionStorage.getItem('language')

fetch('static/config_json/language.json').then(response => {
    return response = response.json()
}).then( data => {
    language_json = data
    if(session_strg_list_lang != null){
        changeLanguagePage(session_strg_list_lang)
    } else {
        sessionStorage.setItem('list_language', JSON.stringify(language_json[0]['list'][0]['esp']))
        sessionStorage.setItem('language', 'esp')
    }  
})

console.log(session_strg_list_lang)
console.log(session_strg_lang)

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
    let home_language = list_lang_.home_page
    text_zpl_btn.textContent = home_language.print_label
    text_fill_btn.textContent = home_language.proces_fill
    text_visco_btn.textContent = home_language.process_visco
    text_modal_info_title.textContent = home_language.title_modal_info
    text_modal_info_body_cred.textContent = home_language.info_fist_p
    text_modal_proc_body_cred.textContent = home_language.scan_creden
    text_modal_proc_body_print.textContent = home_language.scan_creden_print
    text_modal_error_title.textContent = home_language.error_title_modal
    text_modal_error_p1.textContent = home_language.error_body_p1
    text_modal_error_p2.textContent = home_language.error_body_p2

    scan_worker_modal.textContent = home_language.scan_worker_modal
    scan_container_modal.textContent = home_language.scan_container_modal

    mix_modal_info.textContent = home_language.title_improve_modal
    color_label_modal.textContent = home_language.color_label_modal
    viscosity_label_modal.textContent = home_language.viscosity_label_modal
    improvement_btn_start.textContent = home_language.start_improvement_btn
    improvement_btn_close.textContent = home_language.close_improvement_btn
}