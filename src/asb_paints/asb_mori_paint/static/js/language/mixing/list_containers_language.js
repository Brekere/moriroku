let language_json = undefined
let container_list_language = undefined

let text_title = document.getElementById('title')
let text_lang_drop = document.getElementById('lang_drop')
let text_spanish = document.getElementById('spanish')
let text_english = document.getElementById('english')

let text_title_containers = document.getElementById('list_container')
let container_label = document.getElementById('container')

let btn_label_start_fill = document.getElementById('fill_start')
let btn_label_end_process = document.getElementById('end-process')

let session_strg_list_lang = JSON.parse(sessionStorage.getItem('list_language'))
let session_strg_lang = sessionStorage.getItem('language')

fetch('/static/config_json/language.json').then(response => {
    return response = response.json()
}).then( data => {
    language_json = data
})

if(session_strg_lang == 'eng'){
    changeLanguagePage(session_strg_list_lang)
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
    container_list_language = list_lang_.Container_list
    text_title_containers.textContent = container_list_language.title
    container_label.textContent = container_list_language.container
    btn_label_start_fill.textContent = container_list_language.btn_start_fill
    btn_label_end_process.textContent = container_list_language.btn_end_proces
}